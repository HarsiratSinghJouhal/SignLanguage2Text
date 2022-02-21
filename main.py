from typing import final
from xml.etree.ElementPath import find
import cv2
from matplotlib import testing
import numpy as np
import os


orb = cv2.ORB_create()


def preprocess_img(path,minValue = 70):    
    frame = cv2.imread(path)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),2)

    th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    ret, res = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return res


#Import Images
path = 'C:/Users/Harsi/OneDrive/Desktop/CV Bootcamp/My Space/SignLanguage2Text/TrainingDataIMG'
images = []
classNames = []
files = os.listdir(path)

print('Total Classes Detected:',len(files))

for cl in files:
    imgCur = cv2.imread(f'{path}/{cl}')
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
#Import Images



def findDes(images):
    desList = []
    for img in images:
        kp,des = orb.detectAndCompute(img,None)
        desList.append(des)
    return desList
desList = findDes(images)
print(len(desList))



def findID(img,desList,thres=15):
    kp2,des2 = orb.detectAndCompute(img,None)
    bf = cv2.BFMatcher()
    matchList = []
    finalVal = -1
    try:
        for des in desList:
            matches = bf.knnMatch(des,des2,k=2)
            good = []
            for m,n in matches:
                if m.distance < 0.7*n.distance:
                    good.append([m])
            matchList.append(len(good))

    except:
        pass

    if len(matchList) != 0:
        if max(matchList) > thres:
            finalVal = matchList.index(max(matchList))
    return finalVal




#################################################################################################################For Video Input (Start)
# camera = cv2.VideoCapture(0)
# while True:
#     success,img2 = camera.read() 
#     imgOriginal = img2.copy()
#     #img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#     #img2 = preprocess_img(img2)
#     id = findID(img2,desList)

#     if id != -1:
#         cv2.putText(imgOriginal,classNames[id],(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),5)

#     cv2.imshow('Video',imgOriginal) 
#     if cv2.waitKey(1) & 0xFF == ord('q'): 
#         break
# camera.release()                          
# cv2.destroyAllWindows()
#####################################################################################################################For Video Input (End)



#####################################################################################################################Testing Images (Start)
testimg = cv2.imread('C:/Users/Harsi/OneDrive/Desktop/CV Bootcamp/My Space/SignLanguage2Text/TestingImages/1.jpg')
testimg = cv2.resize(testimg,(640,480))
greytestimg = cv2.cvtColor(testimg,cv2.COLOR_BGR2GRAY)
id = findID(greytestimg,desList)
if id != -1:
    cv2.putText(testimg,classNames[id],(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),5)
cv2.imshow('Test Image',testimg) 
cv2.waitKey(0)
cv2.destroyAllWindows()
#####################################################################################################################Testing Images (End)