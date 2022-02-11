import cv2
image=cv2.imread("Messi.jpg")

B,G,R=cv2.split(image)
print(B,shape)