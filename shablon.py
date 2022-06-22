from sqlalchemy.orm import Session

from database_setup import engine, Books, Authors

session = Session(engine)

book = Books(name='Witcher', description='Stories about witcher')
book.authors.append(Authors(name='Volodya', second_name='putin'))

session.add(book)
session.commit()


print()

