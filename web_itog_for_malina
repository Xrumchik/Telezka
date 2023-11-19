import cv2
import pyshine as ps  # pip3 install pyshine==0.0.9
import socket, pickle, struct, imutils
import concurrent.futures

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = '192.168.1.9'
port = 9999
socket_address = (host_ip, port)

# Socket Bind
server_socket.bind(socket_address)# Присвоили сокету ip и port

# Socket Listen
server_socket.listen(5)

HTML = """
<html>
<head>
<title>PyShine Live Streaming</title>
<meta charset="utf-8">




</head>
<body>


<center><h1> Stream for Nikolay </h1></center>
<center><img src="stream.mjpg" width='640' height='480' autoplay playsinline></center>


<button style="position: absolute; bottom: 250; left: 100; width: 200px; height: 50px;" onmousedown="straight()" onmouseup="stop()">Вперед</button>
<button style="position: absolute; bottom: 250; left: 350; width: 200px; height: 50px;" onmousedown="back()" onmouseup="stop()">Назад</button>
<button style="position: absolute; bottom: 250; left: 600; width: 200px; height: 50px;" onmousedown="left()" onmouseup="stop()">Влево</button>
<button style="position: absolute; bottom: 250; left: 850; width: 200px; height: 50px;" onmousedown="right()" onmouseup="stop()">Вправо</button>
<button style="position: absolute; bottom: 250; left: 1100; width: 200px; height: 50px;" onclick="stop()">Стоп</button>
<button style="position: absolute; bottom: 250; left: 1350; width: 200px; height: 50px;" onclick="auto()">Auto</button>


<script>


var xhr = new XMLHttpRequest();


xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
    console.log(this.responseText);
  }
});


function straight () {
    xhr.open("POST", "http://192.168.1.9:4343/straight");
    xhr.send();
    console.log('g');
} 
function back () {
    xhr.open("POST", "http://192.168.1.9:4343/back");
    console.log('b');
    xhr.send();
} 
function left () {
    xhr.open("POST", "http://192.168.1.9:4343/left");
    xhr.send();
    console.log('l');
} 
function right () {
    xhr.open("POST", "http://192.168.1.9:4343/right");
    xhr.send();
    console.log('r');
}
function stop () {
    xhr.open("POST", "http://192.168.1.9:4343/stop");
    xhr.send();
    console.log('s');
}
function auto () {
    xhr.open("POST", "http://192.168.1.9:4343/auto");
    xhr.send();
    console.log('a');
} 

</script>

</body>
</html>
"""


cap=cv2.VideoCapture(0)

def main():
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps, HTML)
    address = ('192.168.1.9', 9000)  # Enter your IP address
    try:
        StreamProps.set_Mode(StreamProps, 'cv2')
        capture = cap
        StreamProps.set_Capture(StreamProps, capture)
        StreamProps.set_Quality(StreamProps, 90)
        server = ps.Streamer(address, StreamProps)
        print('Server started at', 'http://' + address[0])
        server.serve_forever()

    except KeyboardInterrupt:
        capture.release()
        server.socket.close()

def f2():
    while True:
        client_socket, addr = server_socket.accept()  # подключение к сокету
        print('GOT CONNECTION FROM:', addr)
        if client_socket:
            vid = cap  # если есть подключение

            while (vid.isOpened()):  # пока есть видео
                img, frame = vid.read()
                frame = imutils.resize(frame, width=320)
                a = pickle.dumps(frame)
                message = struct.pack("Q", len(a)) + a
                client_socket.sendall(message)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    client_socket.close()


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(main)
        executor.submit(f2)
