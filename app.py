from flask import Flask,request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)


def openpost():
    return "heeey"


@app.route('/process_json', methods=['GET','POST'])
def process_json():
    if request.method == 'POST':
        print(1)
        return openpost()




if __name__=='__main__':
    app.run(host="192.168.1.7", port=4343)
