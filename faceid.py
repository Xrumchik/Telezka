import cv2

face_cas = cv2.CascadeClassifier("/home/pipi/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)


while True:

    success,img=cap.read()

    #img =cv2.imread("face_test1")

    img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=face_cas.detectMultiScale(img_grey,1.1,19)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


    

    cv2.imshow('rez',img)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
