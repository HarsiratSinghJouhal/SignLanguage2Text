from fileinput import filename
import cv2
import os

path = "TrainingDataIMG"
images = []
classNames = []
files = os.listdir(path)

print('Total Classes Detected:',len(files))

for file in files:
    imgCur = cv2.imread(f'{path}/{file}',0)
    cv2.imshow('image',imgCur)
    images.append(imgCur)
    classNames.append(os.path.splitext(file)[0])
    ret,thresholded = cv2.threshold(imgCur,60,255,cv2.THRESH_BINARY)  
    cv2.imshow("Thresholded",thresholded)
    #cv2.imwrite('threshold/'+file,thresholded)

    masked = cv2.bitwise_and(imgCur,imgCur, mask = thresholded) 
    cv2.imshow("Masked", masked)
    cv2.imwrite('masked/'+file,masked)


cv2.waitKey(0)                            # Cleanup after any key is pressed
cv2.destroyAllWindows()