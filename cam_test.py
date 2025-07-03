import cv2
import time
# Open the default webcam
cap = cv2.VideoCapture(0)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3264)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2448)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)
# Check if the camera opened successfully
if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
time.sleep(1)
# Read one frame
for i in range(5):
    ret, frame = cap.read()

    if ret:
        # Save the frame to a file
        cv2.imwrite("captured_image.jpg", frame)
        print("Image saved to 'captured_image.jpg'")
    else:
        print("Failed to capture image")

# Release the webcam
cap.release()