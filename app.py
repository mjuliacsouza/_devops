from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hi, everyones here'


@app.route('/base')
def home1():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
