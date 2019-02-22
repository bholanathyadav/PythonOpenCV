# importing required libraries of opencv 
import cv2 
  
# importing library for plotting 
from matplotlib import pyplot as plt 
  
# reads an input image 
img1 = cv2.imread('C:\\Users\\CA DHEERAJ\\Downloads\\misc\\Lake.png',0)
img2 = cv2.imread('C:\\Users\\CA DHEERAJ\\Downloads\\misc\\Mountain.png',0)
img3 = cv2.imread('C:\\Users\\CA DHEERAJ\\Downloads\\misc\\Snow.png',0)
  
# find frequency of pixels in range 0-255 
histr1 = cv2.calcHist([img1],[0],None,[256],[0,256])
histr2 = cv2.calcHist([img2],[0],None,[256],[0,256])
histr3 = cv2.calcHist([img3],[0],None,[256],[0,256])
  
# show the plotting graph of an image 
plt.plot(histr1)
plt.show()
plt.plot(histr2)
plt.show()
plt.plot(histr3)   
plt.show()