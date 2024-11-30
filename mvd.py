from flask import *
from database import *
from datetime import datetime, timedelta
import random
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

mvd=Blueprint('mvd',__name__)

@mvd.route('/mvdhome')
def mvdhome():

	


	return render_template('mvdhome.html')

@mvd.route('/mvd_view_users',methods=['get','post'])
def mvd_view_users():
	data={}
	if 'districts' in request.form:
		districts=request.form['districts']
		q="select * from user where place like '%s'"%(districts)
		data['view']=select(q)
	else:
		q="select * from user "
		data['view']=select(q)
		
	return render_template('mvd_view_users.html',data=data)

@mvd.route('/view_vehicles',methods=['post','get'])
def view_vehicles():
	data={}
	if 'districts' in request.form:
		districts=request.form['districts']
		q="select * from user inner join vehicles using(user_id) where place like '%s'"%(districts)
		data['view']=select(q)
	else:
		q="select * from vehicles inner join user using(user_id)"
		res=select(q)
		data['view']=res


	return render_template('view_vehicles.html',data=data)

@mvd.route('/mvd_license_home')
def mvd_license_home():
	return render_template('mvd_license_home.html')

@mvd.route('/mvd_view_certificates')
def mvd_view_certificates():
	data={}
	
	


	license_request_id=request.args['license_request_id']
	q="select * from license_files where license_request_id='%s'"%(license_request_id)
	res=select(q)
	data['view']=res
	return render_template('mvd_view_certificates.html',data=data)





@mvd.route('/view_learners_request',methods=['get','post'])
def view_learners_request():
	data={}
	
	q="select * from user inner join licenserequest using(user_id) inner join license_categ using(categid) where place='%s'"%(session['place'])
	res=select(q)
	data['view']=res
	# qv="select status from exam"
	# data['view2']=select(qv)
	


	if 'action' in request.args:
		action=request.args['action']
		license_request_id=request.args['license_request_id']
	else:
		action=None
		

	if action=='approve':
		q="update licenserequest set status='approved' where license_request_id='%s'"%(license_request_id)
		update(q)
		return render_template('schedule_learners.html',data=data)

	if action=='reject':
		q="update licenserequest set status='rejected' where license_request_id='%s'"%(license_request_id)
		update(q)

		return redirect(url_for('mvd.view_learners_request'))
		



	return render_template('view_learners_request.html',data=data)


@mvd.route('/schedule_learners',methods=['post','get'])
def schedule_learners():
	data={}
	license_request_id=request.args['license_request_id']
	q="select * from exam where exam_type='learnersexam' and license_request_id='%s'"%(license_request_id)
	res=select(q)
	data['learners']=res
	
	
	if "schedule" in request.form:
		learnersdate=request.form['date']
		learnerstime=request.form['time']		
		q="insert into exam values(null,'%s','%s','%s','learnersexam','pending')"%(learnersdate,learnerstime,license_request_id)
		insert(q)
		return redirect(url_for('mvd.mvdhome'))

	if 'action' in request.args:
		action=request.args['action']
		exam_id=request.args['exam_id']
	else:
		action=None

	if action=='pass':
		q="update exam set Status='passed' where exam_id='%s'"%(exam_id)
		update(q)
		return redirect(url_for('mvd.view_learners_request'))

	if action=='fail':
		q="update exam set Status='failed' where exam_id='%s'"%(exam_id)
		update(q)

		return redirect(url_for('mvd.view_learners_request'))


	return render_template('schedule_learners.html',data=data)
	
@mvd.route('/schedule_driving_test',methods=['post','get'])
def schedule_driving_test():
	data={}
	

	current_date = datetime.now()

	# Add 10 years
	new_date = current_date + timedelta(days=365 * 20)

	# Format the dates as strings
	current_date_str = current_date.strftime('%Y-%m-%d')
	print("current date::",current_date_str )
	new_date_str = new_date.strftime('%Y-%m-%d')
	print("new date::",new_date_str )

	rand=random.randrange(9999, 100000000000)
	print("rrrrrrrrrrrrrrrrrrrrrrrrr",rand)

	license_request_id=request.args['license_request_id']
	q="select * from exam inner join licenserequest using(license_request_id) inner join user using(user_id) where exam_type='Driving' and license_request_id='%s'"%(license_request_id)
	res=select(q)
	data['test']=res

	

	if "schedule" in request.form:
		license_request_id=request.args['license_request_id']
		testdate=request.form['date']
		testtime=request.form['time']
		
		
	
		q="insert into exam values(null,'%s','%s','%s','Driving','pending')"%(testdate,testtime,license_request_id)
		insert(q)
		return redirect(url_for('mvd.mvdhome'))

	if 'action' in request.args:
		action=request.args['action']
		exam_id=request.args['exam_id']
	else:
		action=None

	if action=='pass':
		user_id=request.args['user_id']
		q="update exam set Status='passed' where exam_id='%s'"%(exam_id)
		update(q)
		qq="update licenserequest set status='passed' where license_request_id='%s'"%(license_request_id)
		update(qq)
		q="insert into license values(null,'%s','%s','%s','%s','%s')"%(rand,user_id,license_request_id,current_date_str,new_date_str)
		insert(q)
		return redirect(url_for('mvd.mvdhome'))

	if action=='fail':
		q="update exam set Status='failed' where exam_id='%s'"%(exam_id)
		update(q)
		return redirect(url_for('mvd.schedule_driving_test'))
	
		
	return render_template('schedule_driving_test.html',data=data)
@mvd.route('/license',methods=['post','get'])
def license():
	if 'add' in request.form:
		licenseno=request.form['licenseno']
		lic_for=request.form['lic_for']
		valid=request.form['valid']
		q="insert into license values(null,'%s','1','%s',curdate(),'%s')"%(licenseno,lic_for,valid)
		insert(q)
	return render_template('license.html')

@mvd.route('/view_vehicle_reg_req')
def view_vehicle_reg_req():
	data={}
	q="select user.first_name,user.place,vehicles.* from user join vehicles on user.user_id=vehicles.user_id where user.place='%s'"%(session['place'])
	res=select(q)
	data['vehicle']=res

	if 'action' in request.args:
		action=request.args['action']
		vehicle_id=request.args['vehicle_id']
	else:
		action=None

	if action=='approve':
		q="update vehicles set status='approved' where vehicle_id='%s'"%(vehicle_id)
		update(q)
		return render_template('mvd_assign_number.html')

	if action=='reject':
		q="delete from  vehicles where vehicle_id='%s'"%(vehicle_id)
		update(q)
		return redirect(url_for('mvd.view_vehicle_reg_req'))

	return render_template('view_vehicle_reg_req.html',data=data)

@mvd.route('/mvd_schedule_inspection_date',methods=['GET', 'POST'])
def mvd_schedule_inspection_date():

	
	if "schedule" in request.form:
		vehicle_id=request.args['vid']
		inspectdate=request.form['inspection_date']
		q="update vehicles set inspection_date='%s' where vehicle_id='%s'"%(inspectdate,vehicle_id)
		update(q)
		return redirect(url_for('mvd.mvdhome'))



	return render_template('mvd_schedule_inspection_date.html')




@mvd.route('/mvd_fancynumber_verification')
def  mvd_fancynumber_verification():
	data={}
	q="select * from vehicles"
	res=select(q)
	data['view']=res

	if 'action' in request.args:
		action=request.args['action']
		vehicle_id=request.args['vehicle_id']
	else:
		action=None

	if action=='approve':
		q="update vehicles set number_status='approved' where vehicle_id='%s'"%(vehicle_id)
		update(q)

	if action=='reject':
		q="delete from vehicles where vehicle_id='%s'"%(vehicle_id)
		update(q)
		return redirect(url_for('mvd.mvd_fancynumber_verification'))
	return render_template('mvd_fancynumber_verification.html',data=data)

@mvd.route('/mvd_assign_number',methods=['get','post'])
def mvd_assign_number():
	vehicle_id=request.args['vehicle_id']
	if 'assign' in request.form:
		rno=request.form['rno']
		q="update vehicles set vehicle_number='%s',number_status='assigned' where vehicle_id='%s'"%(rno,vehicle_id)
		update(q)
		return redirect(url_for('mvd.view_vehicle_reg_req'))
	return render_template('mvd_assign_number.html')

   		

@mvd.route('/view_taxi_permit_req')
def view_taxi_permit_req():
	data={}
	q="select * from permitrequest"
	res=select(q)
	data['taxi']=res

	if 'action' in request.args:
		action=request.args['action']
		vehicle_id=request.args['vehicle_id']
	else:
		action=None
	if action=='v_approve':
		current_date = datetime.now()

	# Add 10 years
		new_date = current_date + timedelta(days=365 *9)

	# Format the dates as strings
		current_date_str = current_date.strftime('%Y-%m-%d')
		print("current date::",current_date_str )
		new_date_str = new_date.strftime('%Y-%m-%d')
		print("new date::",new_date_str )
		w1="insert into taxipermit values(null,'%s','%s','%s')"%(vehicle_id,current_date,new_date)
		insert(w1)
		q="update permitrequest set status='approved' where vehicle_id='%s'"%(vehicle_id)
		re1=update(q)
		return redirect(url_for('mvd.view_taxi_permit_req'))
	if action=='v_reject':
		q="delete from permitrequest where vehicle_id='%s'"%(vehicle_id)
		update(q)


	if action=='approve':
		r="SELECT * FROM USER INNER JOIN `vehicles` USING(user_id) WHERE vehicle_id='%s'"%(vehicle_id)
		data['em']=select(r)
		print("emmmmmmmm",data['em'])
		em1=data['em']
		if em1:
			rr=em1[0]['e_mail']
			print("checkingggg",rr)
		current_date = datetime.now()

	# Add 10 years
		new_date = current_date + timedelta(days=365 * 9)

	# Format the dates as strings
		current_date_str = current_date.strftime('%Y-%m-%d')
		print("current date::",current_date_str )
		new_date_str = new_date.strftime('%Y-%m-%d')
		print("new date::",new_date_str )
		w="update taxipermit set from_date='%s',to_date='%s' where vehicle_id='%s'"%(current_date,new_date,vehicle_id)
		update(w)
		q="update permitrequest set status='approved' where vehicle_id='%s'"%(vehicle_id)
		re1=update(q)
		if re1:
			
			email=rr

					
			pwd="""dear sir/madam
			 your taxi permit is renewed"""



			try:
				gmail = smtplib.SMTP('smtp.gmail.com', 587)
				gmail.ehlo()
				gmail.starttls()
				gmail.login('hariharan0987pp@gmail.com','rjcbcumvkpqynpep')
			except Exception as e:
				print("Couldn't setup email!!"+str(e))

			pwd = MIMEText(pwd)

			pwd['Subject'] = 'Taxipermit renew:'

			pwd['To'] = email

			pwd['From'] = 'hariharan0987pp@gmail.com'


			try:
				gmail.send_message(pwd)

				flash("EMAIL SEND SUCCESFULLY")



			except Exception as e:
				print("COULDN'T SEND EMAIL", str(e))
			else:
				
				flash('ADDED...')
			return redirect(url_for('mvd.view_taxi_permit_req'))

	if action=='reject':
		q="delete from permitrequest where vehicle_id='%s'"%(vehicle_id)
		update(q)
		return redirect(url_for('mvd.view_taxi_permit_req'))

	return render_template('view_taxi_permit_req.html',data=data)

@mvd.route('/mvd_view_complaints')
def mvd_view_complaints():
	data={}
	q="select * from complaint"
	res=select(q)
	data['comp']=res
	return render_template('mvd_view_complaints.html',data=data)
@mvd.route('/mvd_send_reply',methods=['get','post'])
def mvd_send_reply():
	complaint_id=request.args['cid']
	if "send" in request.form:
		reply=request.form['reply']
		q="update complaint set reply='%s' where complaint_id='%s'"%(reply,complaint_id)
		update(q)
		return redirect(url_for('mvd.mvd_view_complaints'))
	return render_template('mvd_send_replay.html')

@mvd.route('/mvd_change_password',methods=['post','get'])
def mvd_change_password():
	if "change" in request.form:
		password=request.form['newpass']
		user=request.form['username']

		q="update login set password='%s' where username='%s'"%(password,user)
		update(q)
		return redirect(url_for('mvd.mvd_change_password'))



	return render_template('mvd_change_password.html')

@mvd.route('/mvd_taxipermit',methods=['get','post'])
def mvd_taxipermit():
	data={}
	vehicle_id=request.args['vehicle_id']

	if "assign" in request.form:
		fd=request.form['fd']
		td=request.form['td']
		
		q="insert into taxipermit values(null,'%s','%s','%s')"%(vehicle_id,fd,td)
		insert(q)
		flash("assigned successfully")
		return redirect(url_for('mvd.view_taxi_permit_req'))
	q="select * from taxipermit where vehicle_id='%s'"%(vehicle_id)
	r=select(q)
	data['view']=r
	return render_template('mvd_taxipermit.html',data=data)

@mvd.route('/mvd_learners_report',methods=['post','get'])
def mvd_learners_report():
	data={}
	if 's_lern' in request.form:
		l_date=request.form['l_date']
		r="select * from exam inner join licenserequest using(license_request_id) inner join user using(user_id) where exam_type='learnersexam' and exam_date like '%s' and place='%s'"%(l_date,session['place'])
		data['view']=select(r)
	else:
		r="select * from exam inner join licenserequest using(license_request_id) inner join user using(user_id) where exam_type='learnersexam' and place='%s'"%(session['place'])
		data['view']=select(r)
	return render_template('mvd_learners_report.html',data=data)
@mvd.route('/mvd_driving_report',methods=['post','get'])
def mvd_driving_report():
	data={}
	if 's_lern' in request.form:
		l_date=request.form['l_date']
		r="select * from exam inner join licenserequest using(license_request_id) inner join user using(user_id) where exam_type='Driving' and exam_date like '%s' and place='%s'"%(l_date,session['place'])
		data['view']=select(r)
	else:
		r="select * from exam inner join licenserequest using(license_request_id) inner join user using(user_id) where exam_type='Driving' and place='%s'"%(session['place'])
		data['view']=select(r)
	return render_template('mvd_driving_report.html',data=data)
@mvd.route('/mvd_inspection_report',methods=['get','post'])
def mvd_inspection_report():
	data={}
	if 'i_date' in request.form:
		l_date=request.form['l_date']
		e="select * from vehicles inner join user using(user_id) where place='%s' and inspection_date like '%s' and inspection_date!='pending' "%(session['place'],l_date)
		data['view']=select(e)
	else:
		e="select * from vehicles inner join user using(user_id) where place='%s' and inspection_date!='pending' "%(session['place'])
		data['view']=select(e)
	return render_template('mvd_inspection_report.html',data=data)
@mvd.route('/mvd_license_report',methods=['get','post'])
def mvd_license_report():
	data={}

	r="select * from license inner join user using(user_id) where place='%s'"%(session['place'])
	data['view']=select(r)
		
	return render_template('mvd_license_report.html',data=data)

@mvd.route('/mvd_payment_report',methods=['get','post'])
def mvd_payment_report():
	data={}
	if 's_type' in request.form:
		type=request.form['type']
		type_date=request.form['type_date']
		e="select * from payment inner join user using(user_id) where place='%s' and type like '%s'and date like '%s'"%(session['place'],type,type_date)
		data['view']=select(e)
	elif 's_month' in request.form:
		month=request.form['month']
		type=request.form['type']
		e="select * from payment inner join user using(user_id) where place='%s' and date like '_____%s___' and type like '%s'"%(session['place'],month,type)
		data['view']=select(e)
	else:
		r="select * from payment inner join user using(user_id) where place='%s'"%(session['place'])
		data['view']=select(r)
	return render_template('mvd_payment_report.html',data=data)

@mvd.route('/logout')
def logout():
	return render_template('home.html')






