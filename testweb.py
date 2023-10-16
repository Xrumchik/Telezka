import cv2
import pyshine as ps  # pip3 install pyshine==0.0.9

HTML = """
<html>
<head>
<title>PyShine Live Streaming</title>
<meta charset="utf-8">




</head>
<body>



<center><h1> Stream for Nikolay </h1></center>


<button style="position: absolute; bottom: 250; left: 300; width: 200px; height: 50px;" onclick="straight()">Вперед</button>
<button style="position: absolute; bottom: 250; left: 550; width: 200px; height: 50px;" onclick="back()">Назад</button>
<button style="position: absolute; bottom: 250; left: 800; width: 200px; height: 50px;" onclick="left()">Влево</button>
<button style="position: absolute; bottom: 250; left: 1050; width: 200px; height: 50px;" onclick="right()">Вправо</button>
<button style="position: absolute; bottom: 250; left: 1300; width: 200px; height: 50px;" onclick="stop()">Стоп</button>


<script>


var xhr = new XMLHttpRequest();


xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
    console.log(this.responseText);
  }
});


function straight () {
    xhr.open("POST", "http://192.168.1.7:4343/straight");
    xhr.send();
} 
function back () {
    xhr.open("POST", "http://192.168.1.7:4343/back");
    xhr.send();
} 
function left () {
    xhr.open("POST", "http://192.168.1.7:4343/left");
    xhr.send();
} 
function right () {
    xhr.open("POST", "http://192.168.1.7:4343/right");
    xhr.send();
}
function stop () {
    xhr.open("POST", "http://192.168.1.7:4343/stop");
    xhr.send();
} 

</script>

</body>
</html>
"""


def main():
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps, HTML)
    address = ('192.168.1.7', 9000)  # Enter your IP address
    try:
        StreamProps.set_Mode(StreamProps, 'cv2')
        capture = '1.mp4'
        server = ps.Streamer(address, StreamProps)
        print('Server started at', 'http://' + address[0])
        server.serve_forever()

    except KeyboardInterrupt:
        capture.release()
        server.socket.close()


if __name__ == '__main__':
    main()
