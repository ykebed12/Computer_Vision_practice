import cv2

# Read image in grayscale
# NOTE: img is read correctly if value is not None
img = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)

# Display the image
cv2.imshow('image', img)

# keyboard binding function that waits for 5000 milliseconds
# if the number was 0, it will read a keyboard button
cv2.waitKey(5000)
cv2.destroyAllWindows()

# Save the image into the compute
cv2.imwrite("lena_copy.png", img)
