import cv2
import numpy as np
from pip._vendor.distlib.compat import raw_input

faceDetection = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

id = raw_input("enter user id")
sampleNum = 0

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetection.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.waitKey(100)
    cv2.imshow("DataSet Creator", img)
    cv2.waitKey(1)
    if sampleNum > 50:
        break
cam.release()
cv2.destroyAllWindows()