import cv2

# Read image
img = cv2.imread('lena.jpg', 1)

# Create image objects with different shapes
red_line_img = cv2.line(img.copy(), (0, 0), (255, 255), (0, 0, 255), 5)
arrowed_line_img = cv2.arrowedLine(img.copy(), (0,0), (255,255), (0,0,255), 10)
rectangle_img = cv2.rectangle(img.copy(), (0,0), (255,255), (0,255,0), -1)

# create image object with text with clone
font = cv2.FONT_HERSHEY_SIMPLEX
line_type = cv2.LINE_AA
text_img = cv2.putText(img, 'OpenCV', (0, 255), font, 4, (255,255,255), 10, line_type)

# Save images as files
cv2.imwrite("Red Line.png", red_line_img)
cv2.imwrite("Arrowed Line.png", arrowed_line_img)
cv2.imwrite("Rectangle.png", rectangle_img)
cv2.imwrite("Text.png", text_img)


cv2.waitKey(0)
cv2.destroyAllWindows()