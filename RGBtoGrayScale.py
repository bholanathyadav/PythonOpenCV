# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:46:43 2019

@author: CA DHEERAJ
"""

import cv2

def main():
    imgpath = "C:\\Users\\CA DHEERAJ\\Downloads\\misc\\house.tiff"
    img = cv2.imread(imgpath, 0)
    
    cv2.imshow('House', img)
    cv2.waitKey(0)
    cv2.destroyWindow('House')
    
if __name__ == "__main__":
    main()