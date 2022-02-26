import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread("car.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = cv2.bilateralFilter(gray, 11,17,17)

canny_edge = cv2.Canny(gray, 100, 200)

_ = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
new = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

contour_with_license_plate = None
license_plate = None
x=None
y=None
w=None
h=None
for contour in contours:
    per = cv2.arcLength(contour, True)
    app = cv2.approxPolyDP(contour, 0.02*per, True)
    if len(app) == 4:
        contour_with_license_plate = app
        x,y,w,h = cv2.boundingRect(contour)
        license_plate = gray[y:y +h, x:x +w]
        break
cv2.imshow("p",license_plate)
cv2.waitKey(0)