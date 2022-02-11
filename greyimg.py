import cv2
image = cv2.imread("Messi.jpg")

greym =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Messi",greym)
cv2.waitKey()
cv2.destroyAllWindows()