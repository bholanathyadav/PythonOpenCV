import cv2
import numpy as np

img = cv2.imread("C:\\Users\\CA DHEERAJ\\Downloads\\misc\\4.2.05.tiff")
retval, threshold = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()