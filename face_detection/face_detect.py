import cv2 as cv
import time

# Load the video
video = cv.VideoCapture(0)
# Loading the classifier for frontal face
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# Loop until user wants to quit
while True:
    
    # ret - bool value if a frame was read or not
    # frame - 3d numpy array of a frame in the video
    ret, frame = video.read()

    # convert frame to grayscale, which becomes a 2d array
    # because face_cascade only works on grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detect faces in grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, 
        minNeighbors=5)

    # Create a rectangle for each face detected on the colored frame
    for (x,y,w,h) in faces:
        frame = cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    # Show colored 3d frame and flip frame horizontally axis for mirror
    # image effect
    cv.imshow('Capturing', cv.flip(frame,1))

    # This will generate a new frame every 200 milliseconds
    # Increasing this number will reduce computer load
    key = cv.waitKey(200)

    # exit loop if user types 'Q'
    if key == ord('q'):
        break


video.release()
cv.destroyAllWindows