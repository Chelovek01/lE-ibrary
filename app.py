import datetime
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_content():  # put application's code here
    if request.method == "POST":
        print(request.form['name'])

    return render_template('home.html')


@app.route('/edit_post/')
def edit_post():
    return render_template('change.html')


if __name__ == '__main__':
    app.run()
