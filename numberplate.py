import cv2
import numpy as np

img=cv2.imread("car.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
filter=cv2.bilateralFilter(gray,11,15,15)
edge=cv2.Canny(filter,170,200)
contor,herf =cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
ctn=sorted(contor,key=cv2.contourArea,reverse=True)
for c in ctn:
    peri=cv2.arcLength(c,True)
    epsilon = 0.018*peri
    approx=cv2.approxPolyDP(c,epsilon,True)
    if len(approx)==4:
        final=cv2.drawContours(img,[approx],-1,(255,0,0),3)
        break

cv2.imshow("Number Plate Detected",img)
cv2.waitKey(0)