import cv2
image = cv2.imread("Messi.jpg")
cv2.imshow("Messi",image)
cv2.waitKey()
cv2.destroyAllWindows()

print(image.shape)
