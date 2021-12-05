from flask import Flask, render_template, request
from flask_cors import CORS
import psycopg2 as pg2
import psycopg2.extras

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

@app.route('/accounts',methods=['GET'])
def accounts():
    return render_template('accounts.html')

@app.route('/services',methods=['GET'])
def services():
    return render_template('services.html')

app.route('/reception/pay_bill',methods=['POST'])
def pay_bill():
    print(request.form)
    #cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #query = "UPDATE BILL SET B_PAYMODE='{}' WHERE B_ID={} AND CUST_ID={}"
    #q = query.format(request.form['paymode'],
    #                request.form['bill_id'],
    #                request.form['customer_id'])
    #cursor.execute(q)
    #conn.commit()
    #cursor.close()
    return {'msg':"If an unpaid bill with the above details exists, it's ben paid!"}

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

    query = "INSERT INTO customer values({},'{}','{}',{},'{}','{}',{},{});"
    q = query.format(max,request.form['fname'],
                    request.form['lname'],request.form['phno'],
                    request.form['email'],request.form['dob'],
                    request.form['nop'],request.form['roomno'])
    #print(q)
    cursor.execute(q)
    conn.commit()
    cursor.close()
    for i in cursor:
        print(i)
    return {'res':'hello'}

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

@app.route('/reception/get_bill',methods=['POST'])
def get_bill():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query = "SELECT B_INFO,B_AMT,B_PAYMODE,B_DATE FROM BILL,CUSTOMER WHERE BILL.CUST_ID=C_ID AND CUSTOMER.C_LNAME='{}' AND C_PHNO={}"
    q = query.format(request.form['cust_lname'],
                    request.form['phno'])
    cursor.execute(q)
    l = []
    for i in cursor:
        l.append(i)
    cursor.close()
    return {'data':l}

@app.route('/reception',methods=['GET'])
def reception():
    return render_template('reception.html')
