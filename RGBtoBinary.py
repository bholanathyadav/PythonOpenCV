import cv2
img = cv2.imread("C:\\Users\\CA DHEERAJ\\Downloads\\misc\\4.1.06.tiff", 0)
cv2.imshow("Gray", img)
cv2.waitKey(0)
ret, bw = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
