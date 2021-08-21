from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLALchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/edit')
def home1():
    return render_template('base.html', todo_list=todo_list)


@app.route('/')
def list():
    todo_list = Todo.query.all()
    return render_template('list.html', todo_list=todo_list)


if __name__ == '__main__':
    app.run()
