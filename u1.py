from flask import *
from database import *
from datetime import datetime
import uuid
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
from datetime import datetime
u1=Blueprint('u1',__name__)

@u1.route('/userhome')
def userhome():
	print("Hello, World!")

	return render_template('userhome.html')

@u1.route('/user_license_home')
def user_license_home():
	return render_template('user_license_home.html')

@u1.route('/request_license',methods=['post','get'])
def request_license():
	data={}
	
	if "submit" in request.form:
		catid=request.form['cat']
		
		r="insert into licenserequest values(null,'%s',now(),'pending','%s')"%(session['user_id'],catid)
		insert(r)
		return redirect(url_for('u1.request_license'))
	q="select * from `licenserequest` where `user_id`='%s'"%(session['user_id'])
	data['viewreq']=select(q)
	c="select * from license_categ"
	data['cat']=select(c)
	return render_template('request_license.html',data=data)

@u1.route('/user_upload_files',methods=['post','get'])
def user_upload_files():
	req_id=request.args.get('req_id')
	if "submit" in request.form:
		idproof=request.files['idproof']
		path1="static/files/"+str(uuid.uuid4())+idproof.filename
		idproof.save(path1)
		photo=request.files['photo']
		path2="static/files/"+str(uuid.uuid4())+photo.filename
		photo.save(path2)
		birth=request.files['birth']
		path3="static/files/"+str(uuid.uuid4())+birth.filename
		birth.save(path3)
		education=request.files['education']
		path4="static/files/"+str(uuid.uuid4())+education.filename
		education.save(path4)
		medical=request.files['medical']
		path5="static/files/"+str(uuid.uuid4())+medical.filename
		medical.save(path5)
		print(idproof,photo,birth,education,medical)
		r="insert into license_files values(null,'%s','%s','%s','%s','%s','%s')"%(req_id,path1,path2,path3,path4,path5)
		insert(r)
		return redirect(url_for('u1.user_payment_home'))
	return render_template('user_upload_files.html',req_id=req_id)

@u1.route('/user_waiting',methods=['get','post'])
def user_waiting():
	if "license_status" in request.form:
		return redirect(url_for('u1.user_license_status'))
	return render_template('user_waiting.html')	

@u1.route('/user_license_status')
def user_license_status():
	data={}
	q="select * from user inner join licenserequest using(user_id) where user_id='%s'"%(session['user_id'])
	data['view']=select(q)
	return render_template('user_license_status.html',data=data)

@u1.route('/view_learners_schedule')
def view_learners_schedule():
	data={}
	license_request_id=request.args['license_request_id']
	# q="SELECT exam.* FROM exam JOIN licenserequest ON exam.license_request_id = licenserequest.license_request_id WHERE exam.exam_type = 'Learners' AND licenserequest.user_id = '%s'"%(session['user_id'])  
	q="select * from exam where license_request_id='%s'"%(license_request_id)
	res=select(q)
	data['exam']=res
	return render_template('view_learners_schedule.html',data=data)


@u1.route('/view_test_schedule')
def view_test_schedule():
	data={}
	q="SELECT exam.* FROM exam JOIN licenserequest ON exam.license_request_id = licenserequest.license_request_id WHERE exam.exam_type = 'Driving' AND licenserequest.user_id = '%s'"%(session['user_id'])
	res=select(q)
	data['test']=res
	return render_template('view_test_schedule.html',data=data)

@u1.route('/vehicle_registration',methods=['post','get'])
def vehicle_registration():

	data={}

	if "add" in request.form:
		vehicletype=request.form['type']
		brandname=request.form['name']
		modelname=request.form['mname']
		seats=request.form['no']
		color=request.form['color']
		date=datetime.now()
		fueltype=request.form['ftype']
		print(vehicletype,brandname,modelname,seats,color,date,fueltype)
		q="insert into vehicles values(null,'%s','%s','%s','%s','%s','%s','%s','pending','%s','registration pending','pending','pending')"%(session['user_id'],vehicletype,brandname,modelname,seats,color,date,fueltype)
		insert(q)
		return redirect(url_for('u1.uservehicle_payment'))


	return render_template('vehicle_registration.html')


@u1.route('/taxi_permit',methods=['post','get'])
def taxi_permit():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		vehicle_id=request.args['vehicle_id']
	else:
		action=None
	if action=="viewtaxi":
		q="insert into permitrequest values(null,'%s',now(),'pending')"%(vehicle_id)
		insert(q)


	
	q="select * from vehicles where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['taxi']=res
	return render_template('taxi_permit.html',data=data)
@u1.route('/userview_taxi_status')
def userview_taxi_status():
	data={}
	vehicle_id=request.args['vehicle_id']
	q="select * from vehicles inner join permitrequest using(vehicle_id) where vehicle_id='%s'"%(vehicle_id)
	data['view']=select(q)
	return render_template('userview_taxi_status.html',data=data)

@u1.route('/assign_number',methods=['post','get'])
def assign_number():
	if "ok" in request.form:
		selected_option=request.form['radioGroup']
		if selected_option=='option1':
			return redirect('fancy_number')
		elif selected_option=='option2':
			return redirect('number')
	return render_template('assign_number.html')

@u1.route('/fancy_number',methods=['post','get'])
def fancy_number():
	if "submit" in request.form:
		number=request.form['num']
		print(number)
		q="update vehicles set vehicle_number='%s'"%(number)
		update(q)
		return redirect('fancy_number')
	return render_template('fancy_number.html')

@u1.route('/number')
def number():
	return render_template('number.html')

@u1.route('/view_registered_vehicles')
def view_registered_vehicles():
	data={}
	q="select * from vehicles where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['vehicle']=res
	return render_template('view_registered_vehicles.html',data=data)


@u1.route('/send_complaint',methods=['post','get'])
def send_complaint():
	data={}
	if "send" in request.form:
		description=request.form['desc']
		date=datetime.now()
		print(description,date)
		q="insert into complaint values(null,'%s','%s','%s','pending')"%(session['user_id'],description,date)
		insert(q)
		return redirect(url_for('u1.send_complaint'))
	q="select * from complaint where `user_id`='%s'"%(session['user_id'])
	data['view']=select(q)
	
	return render_template('send_complaint.html',data=data)

@u1.route('/view_notifications')
def view_notifications():
	data={}
	q="select * from notification where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['not']=res
	return render_template('view_notifications.html',data=data)
@u1.route('/user_payment',methods=['get','post'])
def user_payment():
	if 'vehicle_id' in request.args:
		vehicle_id=request.args['vehicle_id']
		user_id=request.args['user_id']
	if 'payment' in request.form:
		amount=request.form['amount']
		q="insert into payment values(null,'%s','%s','vehicle_registration','%s',curdate())"%(user_id,vehicle_id,amount)
		insert(q)
		return redirect(url_for('u1.userhome'))
	return render_template('user_payment.html')
@u1.route('/user_payment_home')
def user_payment_home():
	data={}
	q="select * from licenserequest inner join license_categ using(categid) where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['view']=res
	if res:
		license_request_id=res[0]['license_request_id']
		data['license_request_id']=license_request_id
		user_id=res[0]['user_id']
		data['user_id']=user_id

	return render_template('user_payment_home.html',data=data)
@u1.route('/uservehicle_payment')
def uservehicle_payment():
	data={}
	q="select * from vehicles inner join user using(user_id) where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['view']=res
	if res:
		vehicle_id=res[0]['vehicle_id']
		data['vehicle_id']=vehicle_id
		user_id=res[0]['user_id']
		data['user_id']=user_id
	return render_template('uservehicle_payment.html',data=data)
@u1.route('/user_license_payment',methods=['get','post'])
def user_license_payment():
	data={}
	if 'license_request_id' in request.args:
		license_request_id=request.args['license_request_id']
		user_id=request.args['user_id']
	if 'payment' in request.form:
		amount=request.form['amount']
		q="insert into payment values(null,'%s','%s','license','%s',curdate())"%(user_id,license_request_id,amount)
		insert(q)
		return redirect(url_for('u1.userhome'))
	q="select * from licenserequest inner join license_categ using(categid) where license_request_id='%s'"%(license_request_id)
	data['view']=select(q)
	return render_template('user_license_payment.html',data=data)

	
from datetime import datetime

@u1.route('/userview_taxi_permit')
def userview_taxi_permit():
	data={}
	vehicle_id = request.args['vehicle_id']
	e="select * from taxipermit where vehicle_id='%s'" % (vehicle_id)
	res2=select(e)
	data['view']=res2
	
	# print("=================================")
	v = "SELECT CURDATE() as date"
	data['check'] = select(v)[0]['date']
	if res2:
		current_date = data['check'].strftime("%Y-%m-%d")
		to_date = res2[0]['to_date'].strftime("%Y-%m-%d")
		print("current_date", current_date)
		print("to_date", to_date)
		if current_date >= to_date:
			# print(";;;;;;;;;;;;;;;;;;;;;")

			email = session['e_mail']
			pwd = """Dear sir/madam,
			Your taxi permit is expired"""

			try:
				
				gmail = smtplib.SMTP('smtp.gmail.com', 587)
				gmail.ehlo()
				gmail.starttls()
				gmail.login('hariharan0987pp@gmail.com', 'rjcbcumvkpqynpep')

				# Create the email message
				email_message = MIMEText(pwd)
				email_message['Subject'] = 'Taxi permit expired:'
				email_message['To'] = email
				email_message['From'] = 'hariharan0987pp@gmail.com'

				# Send the email
				gmail.send_message(email_message)
				return redirect(url_for('u1.userview_taxi_permit,vehicle_id=vehicle_id'))

				# flash("EMAIL SENT SUCCESSFULLY")


			except Exception as e:
				print("COULDN'T SEND EMAIL", str(e))
				

			else:
				# flash('ADDED...')
				return redirect(url_for('u1.taxi_permit'))



	if 'action' in request.args:
		action = request.args['action']
		vehicle_id = request.args['vehicle_id']
		# print("uuuuuuuuuuuuu",vehicle_id)
	else:
		action = None

	if action == "renewtaxi":
		
		# print("fgffffff",session['e_mail'])

		qq = "select * from permitrequest where vehicle_id='%s'" % (vehicle_id)
		res = select(qq)
		# print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",qq)

		if res:
			
			pid = res[0]['vehicle_id']
			qs = "select * from taxipermit where vehicle_id='%s'" % (pid)
			ress = select(qs)
			print("-------------------------",ress)
			if ress:

			# current_date = datetime.strptime(data['check'], "%Y-%m-%d")
			# to_date = datetime.strptime(ress[0]['to_date'], "%Y-%m-%d")
				current_date = data['check'].strftime("%Y-%m-%d")
				to_date = ress[0]['to_date'].strftime("%Y-%m-%d")
				if current_date <= to_date:
					
					email=session['e_mail']
					# print("fhjgjjjjjjjjjj",session['e_mail'])
					pwd="""dear sir/madam
					Your taxi permit not expired"""
					try:
						gmail = smtplib.SMTP('smtp.gmail.com', 587)
						gmail.ehlo()
						gmail.starttls()
						gmail.login('hariharan0987pp@gmail.com','rjcbcumvkpqynpep')
					except Exception as e:
						print("Couldn't setup email!!"+str(e))

					pwd = MIMEText(pwd)

					pwd['Subject'] = 'Taxi permit not expired:'

					pwd['To'] = email

					pwd['From'] = 'hariharan0987pp@gmail.com'

					try:
						gmail.send_message(pwd)

						flash("EMAIL SEND SUCCESFULLY")



					except Exception as e:
						print("COULDN'T SEND EMAIL", str(e))
					else:
						
						flash('ADDED...')
					






					
					return redirect(url_for('u1.taxi_permit'))




				elif current_date > to_date:
					

					email=session['e_mail']
			
					pwd="""dear sir/madam
your taxi permit renewal request is sent"""



					try:
						gmail = smtplib.SMTP('smtp.gmail.com', 587)
						gmail.ehlo()
						gmail.starttls()
						gmail.login('hariharan0987pp@gmail.com','rjcbcumvkpqynpep')
					except Exception as e:
						print("Couldn't setup email!!"+str(e))

					pwd = MIMEText(pwd)

					pwd['Subject'] = 'renewal request'

					pwd['To'] = email

					pwd['From'] = 'hariharan0987pp@gmail.com'

					try:
						gmail.send_message(pwd)

						flash("EMAIL SEND SUCCESFULLY")



					except Exception as e:
						print("COULDN'T SEND EMAIL", str(e))
					else:
						
						flash('ADDED...')
					q = "insert into permitrequest values(null, '%s', curdate(), 'renew')" % (vehicle_id)
					insert(q)
					

				return redirect(url_for('u1.taxi_permit'))









			q = "insert into permitrequest values(null, '%s', curdate(), 'renew')" % (vehicle_id)
			insert(q)
			flash('Your taxi permit has been renewed.')
			return redirect(url_for('u1.taxi_permit'))



	return render_template('userview_taxi_permit.html', data=data)

@u1.route('/materials')
def materials():
	return render_template('materials.html')

@u1.route('/user_payment_report')
def user_payment_report():
	data={}
	r="select * from payment where user_id='%s'"%(session['user_id'])
	data['view']=select(r)
	return render_template('user_payment_report.html',data=data)
@u1.route('/user_License_print')
def user_License_print():
	data={}
	user_id=request.args['user_id']
	r="SELECT * FROM USER INNER JOIN licenserequest USING(user_id) INNER JOIN`license_categ` USING(`categid`) INNER JOIN exam USING(`license_request_id`) inner join license using(user_id) WHERE user_id='%s' AND `exam_type`='Driving' "%(session['user_id'])
	data['view']=select(r)
	return render_template('user_License_print.html',data=data)
@u1.route('/print_li')
def print_li():
	data={}
	user_id=request.args['user_id']
	r="SELECT * FROM USER INNER JOIN licenserequest USING(user_id) INNER JOIN`license_categ` USING(`categid`) INNER JOIN exam USING(`license_request_id`) inner join license using(user_id) WHERE user_id='%s' AND `exam_type`='Driving' "%(session['user_id'])
	data['view']=select(r)
	return render_template('print.html',data=data)
# @u1.route('/logout')
# def logout():
# 	return render_template('home.html')

