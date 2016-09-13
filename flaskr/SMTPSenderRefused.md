# Flask-mail
在Flask Web开发：基于Python的Web引用开发实战——电子邮件 这一节，有关邮箱的设置问题
搞了好久才成功，现在总结下：

刚开始是按照书本设置的Gmail邮箱，但因为墙的原因，并没有成功。通过google了解到可以切
换为国内的126邮箱，于是使用126的邮箱。至于设置，如下：
```Python
import os
#...
app.config['MAIL_SERVER'] ='smtp.126.com' # smtp.126.com是126的主机地址
app.config['MAIL_PORT'] = 25 # 25是126的端口号
app.config['MAIL_USE_TLS'] = True # True表示通过TLS传输
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') # 为安全，设置为从环境变量获取邮箱用户名
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') # 同上，获取邮箱的密码
```
保存电子邮件服务器用户名和密码的两个环境变量要在环境中定义。因为用的是windows，所以按照课本的方式设定环境变量：
```Python
(env) E:\myprojects\flaskr\set MAIL_USERNAME=example@126.com
(env) E:\myprojects\flaskr\set MAIL_PASSWORD=your mail password
```
- 切记是在(env)环境下设置！！

通过命令'(env) $ python hello.py shell'在shell窗口下发送一封测试邮件，以检查配置是否正确：
```Python
>>> from flask.ext.mail import Message
>>> from hello import mail
>>> msg = Message('test subject', sender='you@example.com',
... recipients=['you@example.com'])
>>> msg.body = 'text body'
>>> msg.html = '<b>HTML</b> body'
>>> with app.app_context()
...    mail.send(msg)
...
>>>
```
至此，测试成功！！！

