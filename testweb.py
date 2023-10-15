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


<div style="margin: 500px 0 10px 200px; display:block;">

<button type="bs"  onclick="functionToExecute()">Вперед</button>

</div>

<div style="margin: -20px 0 10px 400px; display:block;">

<button type="bb">Назад</button>

</div>

</div>

<div style="margin: -20px 0 10px 600px; display:block;">

<button type="bb">Влево</button>

</div>

</div>

<div style="margin: -20px 0 10px 800px; display:block;">

<button type="bb">Вправо</button>

</div>


<script>


var xhr = new XMLHttpRequest();


xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
    console.log(this.responseText);
  }
});


function functionToExecute () {
    alert(2);
    xhr.open("POST", "http://192.168.1.7:4343/process_json");
    xhr.send('hello');
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