import cv2
import numpy as np

# Set up a blank canvas
canvas = np.zeros((500, 500, 3), dtype=np.uint8)
circles = []

# Mouse callback function to draw circles
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))  # Add circle center to the list
    elif event == cv2.EVENT_RBUTTONDOWN and circles:
        circles.pop()  # Remove the last circle if it exists

cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas", draw_circle)

while True:
    # Clear canvas and redraw circles
    temp_canvas = canvas.copy()
    for (x, y) in circles:
        cv2.circle(temp_canvas, (x, y), 20, (0, 255, 0), -1)

    cv2.imshow("Canvas", temp_canvas)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('a'):  # Clear all circles
        circles = []

cv2.destroyAllWindows()
