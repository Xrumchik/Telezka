import socket, cv2, pickle, struct

import numpy as np
# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.56.1'  # paste your server ip address here
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
    flaag = 0

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

        if (x > (width / 2 + edge)) and x != 0:
            print("L")
            cv2.rectangle(img, (0, 0), (30, height), (0, 255, 0), -1)
        if (x < (width / 2 - edge)) and x != 0:
            print("R")
            cv2.rectangle(img, (width - 30, 0), (width, height), (0, 255, 0), -1)
    else:
        print("S")
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
client_socket.close()