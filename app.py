from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/getdata', methods=['GET'])
def getdata():
    print (request.form)
    return 'Hello World'

if __name__ == '__main__':
    app.run()
