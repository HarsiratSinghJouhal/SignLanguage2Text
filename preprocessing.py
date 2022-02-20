import cv2
import numpy as np 
import os

dpath = "C:/Users/Harsi/OneDrive/Desktop/CV Bootcamp/My Space/DataCollected/Z"
files = os.listdir(dpath)


def cvt2gray(dpath,files):
    for filename in files:
        filepath = dpath + "/" + filename
        print("Now showing %s"%filename)
        img = cv2.imread(filepath)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        cv2.imshow(filename,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite(dpath + "BW" + str(filename) ,img)
        print("Done!\n")
#cvt2gray(dpath,files)

def threshold(dpath,files,accuracy=75):  
    for filename in files:
        filepath = dpath + "/" + filename
        if "BW" in filepath:
            print("Now thresholding %s"%filename)
            img = cv2.imread(filepath)
            _,thresholded = cv2.threshold(img,accuracy,255,cv2.THRESH_BINARY)  
            cv2.imshow("Thresholded" + filename,thresholded)
            cv2.waitKey(0)                           
            cv2.destroyAllWindows()

#threshold(dpath,files,36) 


minValue = 70
def preprocess(path):    
    frame = cv2.imread(path)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),2)

    th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    ret, res = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return res



def image_cleaning(dpath,files):
        for filename in files:

            filepath = dpath + "/" + filename
            print("Now showing %s"%filename)
            img = cv2.imread(filepath)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            photo = preprocess(filepath)
            cv2.imshow(filename,photo)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imwrite(dpath + "/Curated" + filename,photo)
           

image_cleaning(dpath,files)