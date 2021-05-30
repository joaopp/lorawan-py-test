from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/getdata', methods=['GET'])
def getdata():
    return request.form + 'Hello World'

if __name__ == '__main__':
    app.run()
