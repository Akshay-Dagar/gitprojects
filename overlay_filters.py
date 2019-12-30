import cv2
import numpy as np
import os

cap=cv2.VideoCapture(0)
eyes_cascade=cv2.CascadeClassifier("C:/Users/akshay/zMachineLearning/Challenge_OpenCV_Filters/frontalEyes35x16.xml")               

while 1:
    ret,frame=cap.read()           
    if ret==False:
        continue
    
    eyes=eyes_cascade.detectMultiScale(frame,1.3,5)
    for x,y,w,h in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(227,223,9),2)
    cv2.imshow("Fewery",frame)
    
    key=cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
