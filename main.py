from flask import Flask
from public import public
from admin import admin
from u1 import u1
from mvd import mvd
import smtplib
from email.mime.text import MIMEText   
from flask_mail import Mail

app=Flask(__name__)

app.secret_key="secretkey"
app.register_blueprint(public)
app.register_blueprint(admin)	
app.register_blueprint(u1)
app.register_blueprint(mvd)


mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'hariharan0987pp@gmail.com'

app.config['MAIL_PASSWORD'] = 'rjcbcumvkpqynpep'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.run(debug=True,port=5870)