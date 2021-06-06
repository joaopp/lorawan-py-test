from flask import Flask
from flask import request
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    #file = open("test",'w+')
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

@app.route('/view2')
def view2():
    str_tr = ""
    text = open('test')
    text1 = text.read()
    index = 0
    while index < len(text1):
        index = text1.find("'metadata': {'time': '", index)
        if index == -1:
            break
        str_tr = str_tr + text1[index+22:index+22+19] + "\r\n<br>"
        index += 22 # +2 because len('ll') == 2
    return str_tr


if __name__ == '__main__':
    #app.run()
    app.run(debug=True, host='0.0.0.0') #local test
