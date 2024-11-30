from flask import *
from database import *
import uuid


public=Blueprint('public',__name__)

@public.route('/')
def home():

	return render_template('home.html')

from flask import render_template, redirect, url_for, session, request

@public.route('/login', methods=['post', 'get'])
def login():
    if "login" in request.form:
        a = request.form['uname']
        p = request.form['pass']
        print(a, p)
        q = "select * from login where username='%s' and password='%s'" % (a, p)
        res = select(q)
        print(res)
        if res:
            session['login_id'] = res[0]['login_id']
            if res[0]['type'] == 'admin':
                return redirect(url_for('admin.adminhome'))
            elif res[0]['type'] == 'user':
                q = "select * from user where login_id='%s'" % (session['login_id'])
                res = select(q)
                session['user_id'] = res[0]['user_id']
                session['e_mail'] = res[0]['e_mail']

                return redirect(url_for('u1.userhome'))
            elif res[0]['type'] == 'mvd':
                q = "select * from motorvehicledepartment where login_id='%s'" % (session['login_id'])
                res = select(q)
                session['mvd_id'] = res[0]['mvd_id']
                session['place'] = res[0]['place']

                return redirect(url_for('mvd.mvdhome'))

        # If the login credentials are incorrect, provide an error message.
        error_message = "Invalid username or password. Please try again."
        return render_template('login.html', error_message=error_message)

    return render_template('login.html')



@public.route('/registration',methods=['post','get'])
def registration():
	if "submit" in request.form:
		firstname=request.form['fname']
		lastname=request.form['lname']
		dob=request.form['dob']
		gender=request.form['g']
		house=request.form['hname']
		place=request.form['place']
		pincode=request.form['pin']
		bloodgroup=request.form['blood']
		username=request.form['uname']
		password=request.form['pass']
		photo=request.files['photo']
		email=request.form['email']
		path="static/images/"+str(uuid.uuid4())+photo.filename
		photo.save(path)
		print(firstname,lastname,dob,gender,house,place,pincode,bloodgroup,username,password)
		q="insert login values(null,'%s','%s','user')"%(username,password)
		lid=insert(q)
		q="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,firstname,lastname,dob,gender,house,place,pincode,bloodgroup,path,email)
		insert(q)


	return render_template('registration.html')