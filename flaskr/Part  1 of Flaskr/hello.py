# _*_ coding:utf-8 *_
import os
from threading import Thread
from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_script import Shell, Manager
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)      # 实例化Flask
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] ='smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKR_MAIL_SUBJECT_PREFIX'] = '[Flaskr]'
app.config['FLASKR_MAIL_SENDER'] = 'wqfhpu@126.com'
app.config['FLASKR_ADMIN'] = os.environ.get('FLASKR_ADMIN')


manager = Manager(app)
bootstrap = Bootstrap(app) # 初始化bootsrap模板
moment = Moment(app)       # 初始化Flask-momnet
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref="role", lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<Usr %r>' % self.username
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKR_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                             sender=app.config['FLASKR_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

class NameForm(Form):
    name = StringField("What is your name?", validators=[Required()])
    submit = SubmitField('Submit')


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKR_ADMIN']:
                send_email(app.config['FLASKR_ADMIN'], 'New User',
                          'mail/new_user', user=user)
        else:
            session['known'] = True
           # flash('Look like you have changed yoour name!')
        session['name'] = form.name.data
        #form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
                            form=form, name=session.get('name'),
                            known=session.get('known', False),
                            current_time=datetime.utcnow())


if __name__ == '__main__':
    manager.run()

'''
Flask 提供的 render_template 函数把 Jinja2 模板引擎集成到了程序中。render_template 函数
的第一个参数是模板的文件名。随后的参数都是键值对，表示模板中变量对应的真是值。

'''