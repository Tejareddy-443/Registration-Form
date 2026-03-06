from flask import Flask, render_template,request
import mysql.connector as conn
app=Flask(__name__)
connection=conn.connect(host="localhost",user="root",password="Tejareddy1341",database="registered_users")
@app.route('/')
def home():
    return render_template("Home.html")
@app.route('/menu')
def menu():
    return render_template("Menu.html")
@app.route('/gallary')
def gallary():
    return render_template("Gallery.html")
@app.route('/hours')
def hours():
    return render_template("Hours.html")
@app.route('/reviews')
def reviews():
    return render_template("Reviews.html")
@app.route('/offers')
def offers():
    return render_template("Offers.html")
@app.route('/login')
def Login():
    return render_template("Login.html")
@app.route('/payment')
def payment():
    return render_template("payment.html")
@app.route('/submit_registration',methods=['POST'])
def registration():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    date=request.form['date']
    time=request.form['time']
    guests=request.form['guests']
    
    cursor=connection.cursor()
    query="insert into Customers(name,email,phone,Date_of_reserved,time_of_reserved,No_of_Guests) values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(name,email,phone,date,time,guests))
    connection.commit()
    cursor.execute("select * from Customers")
    data=cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("payment.html",data=data)
if __name__=="__main__":
    app.run(debug=True)
