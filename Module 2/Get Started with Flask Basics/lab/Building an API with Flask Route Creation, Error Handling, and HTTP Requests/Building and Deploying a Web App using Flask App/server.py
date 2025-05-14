from Maths.mathematics import summation, substraction, multiplication
from flask import Flask, make_response, render_template, request

app = Flask("Mathematics Problem Solver")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route('/sum')
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.get.args('num2'))
    result = summation(num1, num2)
    return str(result)

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.get.args('num2'))
    result = substraction(num1, num2)
    return str(result)

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.get.args('num2'))
    result = multiplication(num1, num2)
    return str(result)