import cv2
img = cv2.imread("image.jpg")
cv2.startWindowThread()
cv2.namedWindow("preview")
cv2.imshow("preview", img)
cv2.waitKey(0)