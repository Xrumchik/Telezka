from flask import Flask,request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)


def openpost():
    return "go"


@app.route('/straight', methods=['GET','POST'])
def straight():
    if request.method == 'POST':
        print('go')
        return 'go'

@app.route('/back', methods=['GET','POST'])
def back():
    if request.method == 'POST':
        print('back')
        return 'back'

@app.route('/left', methods=['GET','POST'])
def left():
    if request.method == 'POST':
        print('left')
        return 'left'

@app.route('/right', methods=['GET','POST'])
def right():
    if request.method == 'POST':
        print('right')
        return 'right'

@app.route('/stop', methods=['GET','POST'])
def stop():
    if request.method == 'POST':
        print('stop')
        return 'stop'




if __name__=='__main__':
    app.run(host="192.168.1.7", port=4343)

# curl -X POST -d "data=Hello" http://192.168.1.7:4343/
