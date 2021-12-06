from flask import Flask, render_template, request
from flask_cors import CORS
import psycopg2 as pg2
import psycopg2.extras
from datetime import date

app = Flask(__name__)
CORS(app)

conn_string = "host='localhost' dbname='hoteldb' user='postgres' password='toor'"

try:
	conn = pg2.connect(conn_string)
except:
	print("I am unable to connect to the database")

@app.route('/',methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/reception',methods=['GET'])
def reception():
	return render_template('reception.html')

@app.route('/accounts',methods=['GET'])
def accounts():
	return render_template('accounts.html')

@app.route('/services',methods=['GET'])
def services():
	return render_template('services.html')

@app.route('/reception/customer_checkin',methods=['POST'])
def customer_checkin():
	#cursor = conn.cursor()
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cursor.execute('SELECT MAX(C_ID) FROM customer;')
	max = 0
	for i in cursor:
		max=i
	max = max[0]
	max += 1
	query = "SELECT * FROM customer WHERE c_room = {} AND c_checked_in = TRUE"
	q = query.format(request.form['roomno'])
	cursor.execute(q)
	count = 0
	for i in cursor:
		count += 1
	if count > 0:
		return {'msg':'Room already taken!'}
	query = "INSERT INTO customer values({},'{}','{}',{},'{}','{}',{},{});"
	q = query.format(max,request.form['fname'],
					request.form['lname'],request.form['phno'],
					request.form['email'],request.form['dob'],
					request.form['nop'],request.form['roomno'])
	#print(q)
	cursor.execute(q)
	conn.commit()
	cursor.close()
	return {'msg':'checkin success!'}

@app.route('/reception/customer_checkout',methods=['POST'])
def customer_checkout():
	print(request.form)
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	query = "SELECT B_INFO,B_AMT,B_PAYMODE FROM BILL,CUSTOMER WHERE BILL.CUST_ID=C_ID AND CUSTOMER.C_LNAME='{}' AND C_PHNO={}"
	q = query.format(request.form['cust_lname'],
					request.form['cust_phno'])
	cursor.execute(q)
	bill_items_unpaid = []
	count = 0
	for i in cursor:
		count += 1
		if i[-1] == None:
			bill_items_unpaid.append(i)
	if count == 0:
		return {'msg':'Wrong info!'}
	if len(bill_items_unpaid) > 0:
		return {'msg':'Unpaid bills exist, can\'t checkout!','data':bill_items_unpaid}
	query = "UPDATE CUSTOMER SET C_CHECKED_IN = false WHERE C_LNAME='{}' AND C_PHNO={}"
	q = query.format(request.form['cust_lname'],
					request.form['cust_phno'])
	cursor.execute(q)
	conn.commit()
	cursor.close()
	return {'msg':'Checkout Success!'}

@app.route('/reception/pay_bill',methods=['POST'])
def rec_pay_bill():
	print(request.form)
	#return {'msg':'test'}
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	query = "SELECT * FROM bill WHERE b_paymode IS NOT NULL AND b_id={} AND cust_id={}"
	q = query.format(request.form['customer_id'],
					request.form['bill_id'])
	cursor.execute(q)
	count = 0
	for _ in cursor:
		count += 1
	if count == 0:
		return {'msg':'No such bill due!'}
	query = "UPDATE BILL SET B_PAYMODE ='{}' WHERE CUST_ID={} AND B_ID = {}"
	q = query.format(request.form['paymode'],
					request.form['customer_id'],
					request.form['bill_id'])
	cursor.execute(q)
	conn.commit()
	cursor.close()
	return {'msg':'Bill Paid!'}

@app.route('/reception/get_bill',methods=['POST'])
def get_bill():
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	query = "SELECT B_ID,B_INFO,B_AMT,B_PAYMODE,B_DATE FROM BILL,CUSTOMER WHERE BILL.CUST_ID=C_ID AND CUSTOMER.C_LNAME='{}' AND C_PHNO={}"
	q = query.format(request.form['cust_lname'],
					request.form['phno'])
	cursor.execute(q)
	l = []
	for i in cursor:
		l.append(i)
	cursor.close()
	return {'data':l}

@app.route('/accounts/list',methods=['POST'])
def list_accounts():
	symbols = {'gt':'>','lt':'<','eq':'='}
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	query = "SELECT {} FROM EMPLOYEE WHERE {}"
	f = dict(request.form)
	cols = [f[i] for i in f if i[0] != 'c']
	if len(cols) == 0:
		return {'msg':'No Columns selected!'}
	cond = request.form['condition'] + symbols[request.form['comparison']]
	if request.form['check'].isdigit():
		cond += request.form['check']
	else:
		cond += '"{}"'.format(request.form['check'])
	q = query.format(','.join(cols),
					cond)
	cursor.execute(q)
	l = []
	for i in cursor:
		l.append(i)
	cursor.close()
	return {'data':l,'cols':cols}

@app.route('/accounts/update',methods=['POST'])
def update_accounts():
	return {'msg':'fend working'}

@app.route('/services/list',methods=['POST'])
def list_services():
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	query = "SELECT s_id,s_name,s_description,s_charges FROM services WHERE dept_id={}"
	print(request.form)
	q = query.format(request.form['dept'])
	cursor.execute(q)
	l = []
	for i in cursor:
		l.append(i)
	cursor.close()
	return {'data':l}

@app.route('/services/use',methods=['POST'])
def use_services():
	print(request.form)
	#return {'msg':'test'}
	today = date.today()
	dt = today.strftime("%m/%d/%y")
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cursor.execute('SELECT MAX(B_ID) FROM bill;')
	max = 0
	for i in cursor:
		max=i
	max = max[0]
	max += 1
	query = "SELECT s_name,s_charges FROM services WHERE s_id={}"
	q = query.format(request.form['service_id'])
	cursor.execute(q)
	charges = -1
	desc = ''
	for i in cursor:
		desc,charges = i
	if len(desc) == 0 or charges < 0:
		return {'msg':'Invalid Data'}
	desc += ' x'+str(request.form['quantity'])
	charges = float(charges)*float(request.form['quantity'])
	query = "SELECT c_id FROM customer WHERE c_lname='{}' AND c_phno={} AND c_checked_in=true"
	q = query.format(request.form['cust_lname'],request.form['cust_phno'])
	cursor.execute(q)
	id = -1
	for i in cursor:
		id = i[0]
	if id < 0:
		return {'msg':'No such customer!'}
	query = "INSERT INTO bill (b_info,b_amt,b_id,b_date,cust_id) VALUES ('{}',{},{},'{}',{})"
	q = query.format(desc,charges,max,dt,id)
	cursor.execute(q)
	conn.commit()
	cursor.close()
	return {'msg':'Service added!'}
