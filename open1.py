import cv2

img=cv2.imread('O.jpeg')

##print(img.shape)

new=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))

cv2.imshow('2',new)

cv2.waitKey(0)
