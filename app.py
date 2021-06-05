from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    file = open("test",'w+')
    return 'Hello World - TEST\n'

@app.route('/getdata', methods=['GET','POST'])
def getdata():
    file = open("test","a+")
    file.write(str(request.get_json()) + "\r\n")
    # GET REQUEST with test - return '->' + str(request.args.get("test")) + '<- Hello World - getdata\n'
    return '->' + str(request.get_json()) + '<- Hello World - getdata\n'

@app.route('/setdata')
def setdata():
    return '<form method=GET action=getdata><input type=text name=test></form>'

@app.route('/view')
def view():
    file = open("test")
    return file.read()

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, host='0.0.0.0') #local test
