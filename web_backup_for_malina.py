import cv2
import pyshine as ps  # pip3 install pyshine==0.0.9

import concurrent.futures


HTML = """
<html>

<head>
    <title>PyShine Live Streaming</title>
    <meta charset="utf-8">

    <style>
        body {
            margin: 0;
            padding: 0;
        }

        #video-container {
            width: 50%;
            height: 50%;
            position: relative;
            margin: auto;
        }

        #video {
            width: 100%;
            height: 100%;
            border-radius: 10px;
        }

        #controls {
            width: 100%;
            height: 35%;
            position: absolute;
            bottom: 0;
            left: 0;
            display: flex;
            justify-content: space-around;
            align-items: center;
        }

        button {
            width: 200px;
            height: 60px;
            margin: 0 20px;
            border: none;
            border-radius: 20px;
            background-color: #007bff;
            color: #fff;
            font-size: 24px;
            cursor: pointer;
            padding: auto;
        }

        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-top: 50;
            /* height: 100%; */
        }

        .row {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
        }   
    </style>

</head>

<body>


    <center>
        <h1> Видео от триколясика </h1>
    </center>
    <div id="video-container">
        <img id="video" src="stream.mjpg" width='640' height='480' autoplay playsinline>
    </div>
    <div class="container">
        <div class="row">
            <button class="forward" onmousedown="straight()" onmouseup="stop()">Вперед</button>
        </div>
        <div class="row">
            
            <button class="left" onmousedown="left()" onmouseup="stop()">Влево</button>
            <button class="stop" onclick="stop()">Стоп</button>
            <button class="right" onmousedown="right()" onmouseup="stop()">Вправо</button>
        </div>
        <div class="row">
            
            <button class="backward" onmousedown="back()" onmouseup="stop()">Назад</button>
        </div>
    </div>


    <script>


        var xhr = new XMLHttpRequest();


        xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
                console.log(this.responseText);
            }
        });


        function straight() {
            xhr.open("POST", "http://192.168.225.190:6050/straight");
            xhr.send();
            console.log('g');
        }
        function back() {
            xhr.open("POST", "http://192.168.225.190:6050/back");
            console.log('b');
            xhr.send();
        }
        function left() {
            xhr.open("POST", "http://192.168.225.190:6050/left");
            xhr.send();
            console.log('l');
        }
        function right() {
            xhr.open("POST", "http://192.168.225.190:6050/right");
            xhr.send();
            console.log('r');
        }
        function stop() {
            xhr.open("POST", "http://192.168.225.190:6050/stop");
            xhr.send();
            console.log('s');
        }


    </script>

</body>

</html>
"""


cap=cv2.VideoCapture(0)

def main():
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps, HTML)
    address = ('192.168.225.190', 6030)  # Enter your IP address
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




if __name__ == '__main__':
    main()
