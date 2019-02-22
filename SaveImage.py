# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:21:29 2019

@author: CA DHEERAJ
"""

import cv2

def main():
    imgpath = "C:\\Users\\CA DHEERAJ\\Downloads\\misc\\4.1.01.tiff"
    img = cv2.imread(imgpath)
    
    outpath = "C:\\Users\\CA DHEERAJ\\Desktop\\BNY\\Miscellaneous\\4.1.01.jpg"
    
    cv2.imshow('Lena', img)
    cv2.imwrite(outpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
if __name__ == "__main__":
    main()