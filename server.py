import socket, cv2, pickle, struct, imutils

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 9999
socket_address = (host_ip, port)

# Socket Bind
server_socket.bind(socket_address)# Присвоили сокету ip и port

# Socket Listen
server_socket.listen(5) #
print("LISTENING AT:", socket_address)

# Socket Accept
while True:
    client_socket, addr = server_socket.accept() #подключение к сокету
    print('GOT CONNECTION FROM:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0) #если есть подключение

        while (vid.isOpened()): #пока есть видео
            img, frame = vid.read()
            frame = imutils.resize(frame, width=320)
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()