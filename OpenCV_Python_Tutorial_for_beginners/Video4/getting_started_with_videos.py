import cv2

# Start capturing video from camera
cap = cv2.VideoCapture(0)
# get fourcc code
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 20.0 frames/sec recording with size (640, 480)
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))

print("Cap opened: ", cap.isOpened())
print("Frame Width: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Frame Height: ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    # read each frame
    ret, frame = cap.read()

    # if frame is read succesfully
    if ret == True:
        # record colored frame
        out.write(frame) 

        # create and display grayscale frames
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray_frame)

        # Bit masking to see if user pressed 'q' for quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release all resources
cap.release()
out.release()

cv2.destroyAllWindows()    


