from flask import *
from database import *
from datetime import datetime
import uuid
admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	print("Hello, World!")

	return render_template('adminhome.html')

@admin.route('/AdminAddLicenceCateg',methods=['post','get'])
def AdminAddLicenceCateg():
	data={}
	
	
	if "add" in request.form:
		license=request.form['lic_categ']
		amount=request.form['amount']
		print(license)

		q="insert into license_categ values(null,'%s','%s')"%(license,amount)
		insert(q)

	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
		
	if "update" in request.form:
		categories=request.form['lic_categ']
		amount=request.form['amount']
		
		q="update license_categ set licensecateg='%s',amount='%s' where categid='%s'"%(categories,amount,cid)
		insert(q)
		flash("update successfully")
		return redirect(url_for("admin.adminhome"))
	if action=="update":
		q="select * from license_categ where categid='%s'" %(cid)
		res=select(q)
		data['updatecategorys']=res
	if action=="delete":
		q="delete from  license_categ  where categid='%s'"%(cid)
		delete(q)
		flash("delete successfully")
		return redirect(url_for("admin.adminhome"))

	q="select * from license_categ"
	res=select(q)
	data['view']=res

	return render_template('AdminAddLicenceCateg.html',data=data)

@admin.route('/AdminAddVehicleDept',methods=['post','get'])
def AdminAddVehicleDept():
	data={}
	q="SELECT M.*, L.username FROM motorvehicledepartment M JOIN login L ON M.login_id = L.login_id;"
	res=select(q)
	data['view']=res

	if "add" in request.form:
		place=request.form['place']
		number=request.form['rtnumber']
		phone=request.form['phone']
		email=request.form['email']
		username=request.form['uname']
		password=request.form['pass']
		print(place,number,phone,email,username,password)
		q="insert into login values(null,'%s','%s','mvd')"%(username,password)
		lid=insert(q)
		q="insert into motorvehicledepartment values(null,'%s','%s','%s','%s','%s')"%(lid,place,number,phone,email)
		insert(q)
		return redirect(url_for('admin.AdminAddVehicleDept'))

	if "action" in request.args:
		action=request.args['action']
		mvd_id=request.args['mvd_id']
	else:
		action=None

	if action=='delete':
		q="delete from motorvehicledepartment where mvd_id='%s'"%(mvd_id)
		delete(q)
		return redirect(url_for('admin.AdminAddVehicleDept'))

	if action=='update':
		q="select * from motorvehicledepartment where mvd_id='%s'"%(mvd_id)
		res=select(q)
		data['up']=res
		

	if 'update' in request.form:
		place=request.form['place']
		number=request.form['rtnumber']
		phone=request.form['phone']
		email=request.form['email']
		q="update motorvehicledepartment set place='%s',rt_number='%s',phone='%s',email='%s' where mvd_id='%s'"%(place,number,phone,email,mvd_id)
		update(q)
		return redirect(url_for('admin.AdminAddVehicleDept'))

	return render_template('vehicle_dept_reg.html',data=data)


@admin.route('/view_complaints')
def view_complaints():
	data={}
	q="select * from complaint"
	res=select(q)
	data['comp']=res
	return render_template('view_complaints.html',data=data)

@admin.route('/reply_complaints',methods=['post','get'])
def reply_complaints():
	complaint_id=request.args['cid']
	
	if "send" in request.form:

		

		reply=request.form['reply']

		

		q="update complaint set reply='%s' where complaint_id='%s'"%(reply,complaint_id)
		update(q)
		return redirect(url_for('admin.view_complaints'))



	return render_template('reply_complaints.html',complaint_id=complaint_id)

@admin.route('/view_users',methods=['post','get'])
def view_users():
	data={}
	if 'search' in request.form:
		place=request.form['place']
		q="SELECT user.*, login.username FROM user INNER JOIN login ON user.login_id = login.login_id where place like '%s'"%(place)

		data['view']=select(q)
	else:
		q="SELECT user.*, login.username FROM user INNER JOIN login ON user.login_id = login.login_id"
		res=select(q)
		data['view']=res

	return render_template('view_users.html',data=data)

@admin.route('/payment_report',methods=['post','get'])
def payment_report():
	data={}
	if 's_type' in request.form:
		
		type_date=request.form['type_date']
		e="select * from payment inner join user using(user_id) where date like '%s'"%(type_date)
		data['view']=select(e)
	elif 's_month' in request.form:
		month=request.form['month']
		
		e="select * from payment inner join user using(user_id) where date like '_____%s___'"%(month)
		data['view']=select(e)
	else:
		r="select * from payment inner join user using(user_id) "
		data['view']=select(r)
	return render_template('payment_report.html',data=data)

@admin.route('/notification',methods=['post','get'])
def notification():
	data={}
	

	if "send" in request.form:
		user=request.form['name']
		description=request.form['desc']
		current_datetime=datetime.now()
		print(description,current_datetime)
		q="insert into notification values(null,'%s','%s','%s')"%(user,description,current_datetime)
		insert(q)
		return redirect(url_for('admin.notification'))
	qu="select * from user"
	data['user']=select(qu)
	q="select * from notification"
	res=select(q)
	data['notif']=res

	return render_template('notification.html',data=data)

@admin.route('/change_password',methods=['post','get'])
def change_password():
	if "change" in request.form:
		password=request.form['newpass']
		user=request.form['username']

		q="update login set password='%s' where username='%s'"%(password,user)
		update(q)
		return redirect(url_for('admin.change_password'))



	return render_template('change_password.html')


@admin.route('/logout')
def logout():
	return render_template('home.html')








