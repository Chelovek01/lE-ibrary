import sys
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import Session

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///books-collection.db')

Base = declarative_base()

# association table
library_keywords = Table('library_keywords', Base.metadata,
                         Column('book_id', ForeignKey('all_books.id'), primary_key=True),
                         Column('author_id', ForeignKey('books_authors.id'), primary_key=True))


class Books(Base):
    __tablename__ = "all_books"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    description = Column(Text)

    authors = relationship(
        "Authors", secondary=library_keywords, back_populates="books"
    )

    def __repr__(self):
        return f"Book(id={self.id!r}, name={self.name!r})"


class Authors(Base):
    __tablename__ = "books_authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    second_name = Column(String(255), nullable=False)

    books = relationship("Books", secondary=library_keywords, back_populates="authors")

    def __repr__(self):
        return f"Author(id={self.id!r}, name={self.name!r}, second_name={self.second_name!r})"


Base.metadata.create_all(engine)
