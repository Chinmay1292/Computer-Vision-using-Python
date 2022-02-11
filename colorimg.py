import cv2
image=cv2.imread("Messi.jpg")

B,G,R=cv2.split(image)
print(B.shape)
cv2.imshow("original",image)
cv2.imshow("Red_Image",R)
cv2.imshow("Blue_Image",B)
cv2.imshow("Green_Image",G)
cv2.waitKey()
cv2.destroyAllWindows()