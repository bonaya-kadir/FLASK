from flask import *
import pymysql
# import helper module 
from helper import upload_photo# initialize the app 
app = Flask (__name__)
             
# 1.define your route/endpoint
@app.route("/signup" ,methods=["POST"])
# 2.define signup function 
def signup ():
    # 3.get user inputs from the form 
    username=request.form["username"]
    password=request.form["password"]
    email=request.form["email"]
    phone=request.form["phone"]
    role=request.form["role"]

    # 4.establish connection to database
    connection=pymysql.connect(host="localhost",password="",user="root",database="sokogarden",)

    # 5.define your cursor 
    cursor =connection.cursor()

    # 6.define sql to insert users 
    sql="insert into users (username,password,email,phone,role) value(%s,%s,%s,%s,%s)"

    # 7.define yor data 
    # NB:its coming from step 3 
    data=(username,password,email,phone,role)

    # 8.execute/run query
    cursor.execute(sql,data)

    # 9.commit/save changes 
    connection.commit()

    # 10.give respone to the user 
    return jsonify({"message":"account created successful"})

# 1.Define your route/endpoint
@app.route("/signin" ,methods=["POST"])
# 2.Define signin function
def signin() :
    # 3.get user inputs from the form
    email=request.form["email"]
    password=request.form["password"] 
    # 4.establish connection to database
    connection=pymysql.connect(user="root",host="localhost",password="",database="sokogarden")
    # 5.define your cursor 
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    # 6.sql to select
    sql="select*from users where email=%s and password=%s"
    # 7.define your data 
    # NB:it come from step 3
    data=(email,password)
    # 8.execute/run query
    cursor.execute(sql,data)
    if cursor.rowcount==1 :
        # fetch that user
        loginuser=cursor.fetchone() 
        return jsonify({"message":"login successful" ,"user" :loginuser})
    else :
        return jsonify({"message":"login failed"}) 


# 1.Define your route/endpoint
@app.route("/addproduct",methods=["POST"])
# 2.Define add the product function
def addproduct() :

    # 3.Get products input from the form 
    product_name=request.form["product_name"]
    product_description=request.form["product_description"]
    product_category=request.form["product_category"]
    product_cost=request.form["product_cost"]
    product_photo=request.files["product_photo"]

    # 4.establish connection to database 
    connection=pymysql.connect(host="localhost",password="",user="root",database="sokogarden")

    # 5.Define your cursor 
    cursor=connection.cursor()

    # 6.Define sql to insert products 
    sql="insert into products(product_name,product_description,product_category,product_cost,product_photo)values(%s,%s,%s,%s,%s)"

    # 7.Define your data 
    # comes from number 3
    data=(product_name,product_description,product_category,product_cost,upload_photo(product_photo))

    #8. execute/run query
    cursor.execute(sql,data)

    # 9.commit /save changes 
    connection.commit()

    # 10.give response to products 
    return jsonify({"message":"products added successfully"})
    

@app.route("/getproducts")
def getproducts() :
    return "Welcome to get products"


# run the application 
app.run(debug=True)