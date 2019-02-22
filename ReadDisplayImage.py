import cv2

def main():
    
    imgpath = "C:\\Users\\CA DHEERAJ\\Downloads\\misc\\4.1.01.tiff"
    img = cv2.imread(imgpath)
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()