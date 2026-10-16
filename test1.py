from flask import *
# initialize the app 
app = Flask (__name__)
             
# define your route/endpoint
@app.route("/login")
# define login function 
def login ():
    return "welcome to our login"

# run the application 
app.run(debug=True)