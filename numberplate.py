import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread("car.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = cv2.bilateralFilter(gray, 11,17,17)
