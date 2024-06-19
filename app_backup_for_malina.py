from flask import Flask, request
from flask_cors import CORS
import serial
import socket, cv2, pickle, struct
import numpy as np
import time
import concurrent.futures
import threading
app = Flask(__name__)
CORS(app)

data = b""
payload_size = struct.calcsize("Q")
try:
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
except:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()







@app.route('/straight', methods=['GET', 'POST'])
def straight():
    if request.method == 'POST':
        print('go')
        ser.write(b'g\n')
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        return 'go'


@app.route('/back', methods=['GET', 'POST'])
def back():
    if request.method == 'POST':
        print('back')
        ser.write(b'b\n')
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        return 'back'


@app.route('/left', methods=['GET', 'POST'])
def left():
    if request.method == 'POST':
        print('left')
        ser.write(b'l\n')
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        return 'left'


@app.route('/right', methods=['GET', 'POST'])
def right():
    if request.method == 'POST':
        print('right')
        ser.write(b'r\n')
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        return 'right'


@app.route('/stop', methods=['GET', 'POST'])
def stop():
    if request.method == 'POST':
        print('stop')
        global flaaag
        flaaag=0
        ser.write(b's\n')
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        return 'stop'






if __name__ == '__main__':
    app.run(host="192.168.225.190", port=6050)
