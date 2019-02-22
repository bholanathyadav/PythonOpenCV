import cv2
import numpy as np

img1 = cv2.imread("C:\\Users\\CA DHEERAJ\\Downloads\\misc\\4.1.06.tiff")
img2 = cv2.imread("C:\\Users\\CA DHEERAJ\\Downloads\\misc\\4.1.08.tiff")

#add = cv2.add(img1, img2)
add = img1+img2

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()