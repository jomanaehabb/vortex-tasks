import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):  # Quit
        break
    elif key == ord('r'):  # Rotate 90 degrees
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif key == ord('c'):  # Save the frame as an image
        cv2.imwrite("saved_frame.jpg", frame)
        print("Frame saved as 'saved_frame.jpg'")
    elif key == ord('s'):  # Start saving video stream
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('saved_video.avi', fourcc, 20.0, (640, 480))
        out.write(frame)
        print("Saving video stream as 'saved_video.avi'")
    elif key == ord('g'):  # Convert to grayscale
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif key == ord('h'):  # Convert to HSV
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    elif key == ord('x'):  # Show grayscale, HSV, rotated, and original
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        rotated = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        combined = np.hstack([frame, hsv, rotated])
        cv2.imshow("Combined Frames", combined)
        continue  # Skip the default display to avoid overlap
    elif key == ord('z'):  # Show only the original frame
        cv2.imshow("Original Frame", frame)
        continue

    # Display frame
    cv2.imshow("Camera Feed", frame)

cap.release()
cv2.destroyAllWindows()
