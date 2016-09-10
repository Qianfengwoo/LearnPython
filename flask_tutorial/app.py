# _*_ coding:utf-8 _*_
from flask import Flask, render_template, redirect, \
    url_for, request, session, flash, g
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps

# import sqlite3

app = Flask(__name__)

app.secret_key = 'my precious'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

# create the sqlalchemy object
db = SQLAlchemy(app)


# app.database = 'sample.db'


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('login'))

    return wrap


@app.route('/')
@login_required
def home():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = []
    for row in cur.fetchall():
        posts.append(dict(title=row[0], description=row[1]))
    # posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('index.html', posts=posts)
    # return "<h1 styles='color: green'>Hello, Flask!</h1>"


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials,Please try again.'
        else:
            session['logged_in'] = True
            flash("You were just logged in!")
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # 当用户登出的时候，可以将网站保存的session给去掉
    flash("You were just logged out!")
    return redirect(url_for('welcome'))


# def connect_db():
#    return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run(debug=True)
