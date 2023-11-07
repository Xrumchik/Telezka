from flask import Flask,request
from flask_cors import CORS
import serial
import socket, cv2, pickle, struct
import numpy as np
import time

app=Flask(__name__)
CORS(app)



def dist():
    print("kl")
    while True:

        hsv_min = np.array((22, 154, 127), np.uint8)
        hsv_max = np.array((88, 180, 218), np.uint8)
        img=frame
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
            cv2.circle(img, (x, y), 10, (0, 0, 255), -1)

            if (x <= (width / 2 + edge)+10)and (x >= (width / 2 - edge)-10) and x != 0:
                print("G")

            if (x > (width / 2 + edge)+10) and x != 0:
                print("L")
                cv2.rectangle(img, (0, 0), (30, height), (0, 255, 0), -1)

            if (x < (width / 2 - edge)-10) and x != 0:
                print("R")
                cv2.rectangle(img, (width - 30, 0), (width, height), (0, 255, 0), -1)
        else:
            print("S")
        cv2.imshow('result', img)
        
    return "salam"

try:
    ser=serial.Serial('/dev/ttyACM1',9600,timeout=1)
except:
    ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
ser.flush()
ser.write(b'heyaaa\n')
line=ser.readline().decode('utf-8').rstrip()
print(line)

@app.route('/straight', methods=['GET','POST'])
def straight():
    if request.method == 'POST':
        print('go')
        ser.write(b'g\n')
        line=ser.readline().decode('utf-8').rstrip()
        print(line)
        return 'go'

@app.route('/back', methods=['GET','POST'])
def back():
    if request.method == 'POST':
        print('back')
        ser.write(b'b\n')
        line=ser.readline().decode('utf-8').rstrip()
        print(line)
        return 'back'

@app.route('/left', methods=['GET','POST'])
def left():
    if request.method == 'POST':
        print('left')
        ser.write(b'l\n')
        line=ser.readline().decode('utf-8').rstrip()
        print(line)
        return 'left'

@app.route('/right', methods=['GET','POST'])
def right():
    if request.method == 'POST':
        print('right')
        ser.write(b'r\n')
        line=ser.readline().decode('utf-8').rstrip()
        print(line)
        return 'right'

@app.route('/stop', methods=['GET','POST'])
def stop():
    if request.method == 'POST':
        print('stop')
        dist()
        return 'stop'




if __name__=='__main__':
    app.run(host="192.168.137.7", port=4343)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = '192.168.1.7'  # paste your server ip address here
    port = 9999
    client_socket.connect((host_ip, port))  # подключаемся к сокету
    data = b""
    payload_size = struct.calcsize("Q")
    while True:
        while len(data) < payload_size:
                packet = client_socket.recv(4 * 1024)  # 4K
                if not packet: break
                data += packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(data) < msg_size:
                data += client_socket.recv(4 * 1024)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    client_socket.close()
    
