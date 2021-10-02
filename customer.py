import pymysql
from flask import Flask,render_template,request,session


app=Flask(__name__)
app.secret_key = 'your secret key'
@app.route('/')
def home():
    return '''<div style="background-color:lightpink";><h1>CUSTOMER DATA ENTRY FORM</h1></div>
              <div style="background-color:lightyellow";><a href="/login" >login here</a></div><br>
              <div style="background-color:cyan";><a href="/register">register here</a></div>'''

@app.route('/register')
def register():
    return render_template('customer.html')

@app.route('/insertrecord',methods=['POST','GET'])
def insert():
    msg=""
    if request.method=='POST':
        try:
            custid=request.form["txtcid"]
            username=request.form["txtcname"]
            password=request.form["txtpassword"]
            age=request.form["txtage"]
            city=request.form["txtcity"]
            email=request.form["txtemail"]
            con=pymysql.connect(host="localhost",user='root',password='',database='login')
            cur=con.cursor()
            cur.execute("INSERT INTO CUSTOMER1 values(%s,%s,%s,%s,%s,%s)",(custid,username,password,age,city,email))
            con.commit()
            msg="record saved successfully"
        except:
            msg="record not saved"
        finally:
            con.close()
            return render_template('success.html',msg=msg)

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/add',methods=['POST','GET'])
def validation():
    msg = ''
    if request.method == 'POST':
        try:
            u=request.form["username"]
            p=request.form["password"]
            con=pymysql.connect(host="localhost",user='root',password='',database='login')
            cursor = con.cursor()
            cursor.execute('SELECT * FROM customer1 WHERE username = %s AND password = %s', (u,p))
            customer = cursor.fetchall()
            msg = 'succesfully entered'
            
        except:
            msg="error"
            return render_template("error.html",smsg=msg)
        finally:
            con.close()
            return render_template('my_success.html',result=customer)
@app.route('/delete')
def del_data():
    return render_template('delete.html')

@app.route('/delete1',methods=['POST','GET'])
def delete_record1():
    msg=" "
    if request.method=='POST' :
        try:
            uname=request.form["uname"]
            #create connection
            con= pymysql.connect(host="localhost", user='root',password='',database='login')   
            cur = con.cursor()
            cur.execute("Delete from customer1 where username=%s",(uname))
            con.commit()  #delete record permanently into table
            res=cur.fetchall()#fetching all data into tuple
            msg = "Customer Record successfully Deleted"  
        except:  
            msg = "We can not delete the customer data into table"
            return render_template("error.html",smsg=msg)
        finally:
            con.close()
            return render_template("my_display2.html",dresult=res)
@app.route('/view_all')
def displayall():
     #create connection
    try:
            con= pymysql.connect(host="localhost", user='root',password='',database='login')   
            cur = con.cursor()
            cur.execute("Select * from customer1")
            result=cur.fetchall() #create tuple  of result which hold the all records from table
            con.close()
            return render_template('display.html',result=result)
    except:
        msg="error"
        return render_template("error.html",smsg=msg)
@app.route('/update')
def update_data():
    return render_template('update.html')

@app.route('/update1',methods=['POST','GET'])
def update_record1():
    msg=" "
    if request.method=='POST' :
        try:
            uname=request.form["uname"]
            pwd=request.form["pwd"]
            #create connection
            con= pymysql.connect(host="localhost", user='root',password='',database='login')   
            cur = con.cursor()
            cur.execute("Update customer1 set password=%s where username=%s",(pwd,uname))
            con.commit()  #Update record permanently into table
            res=cur.fetchall()#fetching all data into tuple
            msg = "Customer Record successfully Updated"  
        except:  
            msg = "We can not Update the customer data into table"
            return render_template("error.html",smsg=msg)
        finally:
            con.close()
            return render_template("showupdate.html")








    
app.run(debug=True)
