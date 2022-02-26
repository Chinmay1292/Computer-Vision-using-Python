import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread("car.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = cv2.bilateralFilter(gray, 11,17,17)

canny_edge = cv2.Canny(gray, 100, 200)

_, contours, new = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
cv2.imshow("p",canny_edge)
cv2.waitKey(0)