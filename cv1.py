import cv2
import numpy as np

# Create four 50x50 colored images
red_square = np.full((50, 50, 3), (0, 0, 255), dtype=np.uint8)    # Red
green_square = np.full((50, 50, 3), (0, 255, 0), dtype=np.uint8)  # Green
blue_square = np.full((50, 50, 3), (255, 0, 0), dtype=np.uint8)   # Blue
yellow_square = np.full((50, 50, 3), (0, 255, 255), dtype=np.uint8) # Yellow

# Combine them to make a 100x100 image
top_row = np.hstack((red_square, green_square))
bottom_row = np.hstack((blue_square, yellow_square))
combined_image = np.vstack((top_row, bottom_row))

# Resize the image to 200x200
resized_image = cv2.resize(combined_image, (200, 200))

# Display the image
cv2.imshow("Combined and Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
