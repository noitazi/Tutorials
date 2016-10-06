import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
shoulder_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

img = cv2.imread('noitaziBodyDetect.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height = img.shape[0]
width = img.shape[1]

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    # img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    shoulders = shoulder_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in shoulders:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

resized_img = cv2.resize(img, (width/5, height/5))

cv2.imshow('img',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()