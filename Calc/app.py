from flask import Flask
app = Flask(__name__)

from operations import add, sub, mult, div

@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int (request.args.get('b'))
    result = add(a, b)

    return str(result)

@app.route('/sub')
def subtract():
    a = int(request.args.get('a'))
    b = int (request.args.get('b'))
    result = subract(a, b)

    return str(result)
    
@app.route('/mult')
def multiply():
    a = int(request.args.get('a'))
    b = int (request.args.get('b'))
    result = multiply(a, b)

    return str(result)

@app.route('/div')
def divide():
    a = int(request.args.get('a'))
    b = int (request.args.get('b'))
    result = divide(a, b)

    return str(result)
    




