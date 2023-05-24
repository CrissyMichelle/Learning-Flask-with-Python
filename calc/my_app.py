from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def add_func():
    a = int(request.args['a'])
    b = int(request.args['b'])
    calc = add(a, b)
    return f"<h1>Addition of {a} and {b} equals {calc}</h1>"

@app.route('/sub')
def sub_func():
    a = int(request.args['a'])
    b = int(request.args['b'])
    calc = sub(a, b)
    return f"<h1>Subtraction of {b} from {a} equals {calc}</h1>"

@app.route('/mult')
def mult_func():
    a = int(request.args['a'])
    b = int(request.args['b'])
    calc = mult(a, b)
    return f"<h1>Multiplication of {a} and {b} equals {calc}</h1>"

@app.route('/div')
def div_func():
    a = int(request.args['a'])
    b = int(request.args['b'])
    calc = div(a, b)
    return f"<h1>Division of {a} by {b} equals {calc}</h1>"

#Consolidate the above routes into a single decorator that handles all 4 functions
operators = {
    #this dictionary maps the math calculation to the operations.py function
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}
#Extend the URL to include an operator parameter
@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    calc = operators[oper](a, b)
    return f"<h1>{oper} of {a} and {b} equals {calc}</h1>"

