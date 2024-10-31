import cv2
import numpy as np

# Load an image (substitute with the path to your card image)
image = cv2.imread("card_image.png")

points = []

# Mouse callback to capture four points
def select_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) == 4:
            warp_card()

def warp_card():
    global points, image
    pts1 = np.float32(points)
    width, height = 300, 400
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    # Get transformation matrix and warp
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    warped = cv2.warpPerspective(image, matrix, (width, height))

    cv2.imshow("Warped Card", warped)

cv2.imshow("Original Image", image)
cv2.setMouseCallback("Original Image", select_points)

cv2.waitKey(0)
cv2.destroyAllWindows()
