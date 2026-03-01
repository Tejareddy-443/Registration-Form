from flask import Flask, render_template,request
import mysql.connector as conn
app=Flask(__name__)
connection=conn.connect(host="localhost",user="root",password="Tejareddy1341",database="registered_users")
@app.route('/')
def home():
    return render_template("Home.html")
@app.route('/submit_registration',methods=['POST'])
def registration():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    confirm_password=request.form['confirm_password']
    if password!=confirm_password:
        return "password and Confirm password do not match"
    cursor=connection.cursor()
    query="insert into users(name,email,password) values(%s,%s,%s)"
    cursor.execute(query,(name,email,password))
    cursor.execute("select * from users")
    data=cursor.fetchall()
    return render_template("users.html",data=data)
if __name__=="__main__":
    app.run(debug=True)
