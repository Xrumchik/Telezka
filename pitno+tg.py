import cv2
import numpy as np
import serial
import time
import telepot   
from telepot.loop import MessageLoop    
command=''
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message

    print ('Received:', command)
    if command == 'Go':
        bot.sendMessage (chat_id, str("Ok, go!"))
        ser.write(b"G")
        print("G")
    elif command == 'L':
        bot.sendMessage (chat_id, str("Ok, left!"))
        print("L")
        ser.write(b"L")
    elif command == 'R':
        bot.sendMessage (chat_id, str("Ok, right!"))
        ser.write(b"R")
        print("R")
    elif command == 'S':
        bot.sendMessage (chat_id, str("Ok, stop!"))
        ser.write(b"S")
        print("S")
    elif command == 'D':
        ser.write(b"D")
        print("D")
        bot.sendMessage (chat_id, str("Ok, automatically!"))
    elif command == 'B':
        ser.write(b"B")
        print("B")
        bot.sendMessage (chat_id, str("Ok, back!"))

bot = telepot.Bot('6212498537:AAHCjs1CViLcsXH7D1kYekZPZV6oPFNudWg')

MessageLoop(bot, handle).run_as_thread()

cv2.namedWindow( "result" )

cap =  cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)


# HSV фильтр для зеленых объектов из прошлого урока

flaag=0

hsv_min = np.array((22,154,127), np.uint8)
hsv_max = np.array((88,180,218), np.uint8)

while True:
    line = ser.read()
    print(line)
    flag, img = cap.read()
    height,width = img.shape[:2]
    edge=10
    # преобразуем RGB картинку в HSV модель
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    # применяем цветовой фильтр
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)

    # вычисляем моменты изображения
    moments = cv2.moments(thresh, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']
    x=0
    #print(line)
    #print(flaag)
    if command=='D' and flaag==0:
        flaag=1
    elif command=='S' and flaag==1:
        flaag=0

    # будем реагировать только на те моменты,
    # которые содержать больше 100 пикселей
    if dArea > 100:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(img, (x, y), 10, (0,0,255), -1)
        
        if (x>(width/2+edge)) and x!=0 and flaag==1:
            ser.write(b"L")
            print("L")
            cv2.rectangle(img, (0,0), (30,height), (0,255,0), -1)
        if (x<(width/2-edge)) and x!=0 and flaag==1:
            ser.write(b"R")
            print("R")
            cv2.rectangle(img, (width-30,0), (width,height), (0,255,0), -1)
    elif flaag==1:
        ser.write(b"S")
        print("S")

    
    cv2.imshow('result', img) 
 
    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()


#27,179,136
#55,239,232  cv2.VideoCapture(0)
