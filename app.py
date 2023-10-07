from flask import Flask,request

app=Flask(__name__)

def openget():
    return "sdfsdf"

def openpost():
    return "sdfsdf"


@app.route('/process_json', methods=['GET','POST'])
def process_json():
    if request.method == 'POST':
        print(1)
        return openpost()
    if request.method == 'GET':
        print(2)
        return openget()


if __name__=='__main__':
    app.run(host="192.168.137.193", port=4343)
