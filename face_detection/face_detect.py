import cv2 as cv
import time

video = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")


while True:
    
    time.sleep(0.2)

    ret, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

    for (x,y,w,h) in faces:
        frame = cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv.imshow('Capturing', frame)
    key = cv.waitKey(1)

    if key == ord('q'):
        break


video.release()
cv.destroyAllWindows