import cv2

def main():
    imgpath1 = "C:\\Users\\CA DHEERAJ\\Downloads\\misc\\4.1.01.tiff"
    imgpath2 = "C:\\Users\\CA DHEERAJ\\Downloads\\misc\\4.1.04.tiff"
    img1 = cv2.imread(imgpath1)
    img2 = cv2.imread(imgpath2)
    
    dst = cv2.addWeighted(img1,0.5,img2,0.5,0)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()