from flask import *

# initialize the application
app=Flask(__name__)

# define your route/endpoint
@app.route("/home")
# deine your function
def home():
    return "Welcome to home"

@app.route("/lab1")
def lab1() :
    return "Welcome to lab1"

@app.route("/safaricom")
def safaricom() :
    return "Welcome to safaricom.How can we help you"

@app.route("/about")
def about():
    return "Welcome to about us"

@app.route("/contact")
def contact():
    return "Contact us for more information"

@app.route("/Students")
def students():
    return "Welcome to our students portal"

@app.route("/mpesa")
def mpesa():
    return "Welcome to M-pesa Services"

@app.route("/services")
def services():
    return "Here are the services we offer"

@app.route("/addition" , methods=["POST"])
def addition () :
    number1 =request.form["number1"]   
    number2 =request.form["number2"]
    answer =int(number1)+int(number2)
    return jsonify({"sum":answer})

@app.route("/subtraction" , methods=["POST"])
def subtraction () :
    number1 = request.form["number1"]
    number2 =request.form["number2"]
    answer =int(number1)-int(number2)
    return jsonify({"difference":answer})

@app.route("/multiplication" , methods=["POST"])
def multiplication () :
    number1 = request.form["number1"]
    number2 =request.form["number2"]
    answer =int(number1)*int(number2)
    return jsonify({"multiple":answer})

@app.route("/division" , methods=["POST"])
def division () :
    number1 = request.form["number1"]
    number2 =request.form["number2"]
    answer =int(number1)/int(number2)
    return jsonify({"div":answer})

@app.route("/modulus" , methods=["POST"])
def modulus () :
    number1 = request.form["number1"]
    number2 =request.form["number2"]
    answer =int(number1)%int(number2)
    return jsonify({"module":answer})

@app.route("/exponent" , methods=["POST"])
def exponent () :
    number1 = request.form["number1"]
    number2 =request.form["number2"]
    answer =int(number1)**int(number2)
    return jsonify({"expo":answer})

@app.route("/intergerdivision" , methods=["POST"])
def interger () :
    number1 = request.form["number1"]
    number2 =request.form["number2"]
    answer =int(number1)//int(number2)
    return jsonify({"interger":answer})

































# run the application 
app.run(debug=True)