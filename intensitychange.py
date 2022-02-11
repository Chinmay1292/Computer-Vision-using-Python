import cv2

image = cv2.imread("Messi.jpg")
B,G,R = cv2.split(image)
merge = cv2.merge([B,G,R+100])
cv2.imshow("merged",merge)
cv2.waitKey()
cv2.destroyAllWindows()