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
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.1.9'  # paste your server ip address here
port = 9999
client_socket.connect((host_ip, port))  # подключаемся к сокету
data = b""
payload_size = struct.calcsize("Q")
try:
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
except:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()



flaaag=0



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


def f2():
    global data
    global flaaag
    while flaaag:
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 4K
            if not packet:
                break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        flaag = 0

        hsv_min = np.array((22, 154, 127), np.uint8)
        hsv_max = np.array((88, 180, 218), np.uint8)
        img = frame
        height, width = img.shape[:2]
        edge = 10
        # преобразуем RGB картинку в HSV модель
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # применяем цветовой фильтр
        thresh = cv2.inRange(hsv, hsv_min, hsv_max)

        # вычисляем моменты изображения
        moments = cv2.moments(thresh, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']
        x = 0
        # print(line)

        # будем реагировать только на те моменты,
        # которые содержать больше 100 пикселей
        if dArea > 100:
            x = int(dM10 / dArea)
            y = int(dM01 / dArea)

            if (x <= (width / 2 + edge) + 10) and (x >= (width / 2 - edge) - 10) and x != 0:
                print("G")
                ser.write(b'g\n')
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
            if (x > (width / 2 + edge) + 10) and x != 0:
                print("L")
                ser.write(b'l\n')
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
            if (x < (width / 2 - edge) - 10) and x != 0:
                print("R")
                ser.write(b'r\n')
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
        else:
            print("S")
            ser.write(b's\n')
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    client_socket.close()

@app.route('/auto', methods=['GET', 'POST'])
def auto():
    if request.method == 'POST':
        print('auto')
        global flaaag
        flaaag=1
        f2()
        ser.write(b's\n')
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        return 'auto'




if __name__ == '__main__':
    app.run(host="192.168.1.9", port=4343)
