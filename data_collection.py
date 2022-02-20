import os
import cv2
import numpy as np

cd = "C:/Users/Harsi/OneDrive/Desktop/CV Bootcamp/My Space/"
path = "DataCollected/FullData"
dirDATACOLLECTED = os.path.join(cd,path)

alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U",'V',"W","X","Y","Z"]
alpha_path = [dirDATACOLLECTED + "/" + a for a in alphabets]

counter = 0
camera = cv2.VideoCapture(0)
while(True):
    ret, frame = camera.read()             
    cv2.imshow('Data Collection',frame)           
    
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.imwrite(alpha_path[25]+ "/" +str(counter)+".jpg",frame) 
        counter += 1 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

camera.release()                          
cv2.destroyAllWindows()