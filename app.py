from flask import Flask
app = Flask(__name__) 

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def home():
    return "This is home page"

# import controller.user_controller as user_controller
# import controller.product_controller as product_controller
# expect this write this
# from controller import user_controller, product_controller
# expect this write this by making controller as python package
from controller import *

