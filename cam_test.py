import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Read one frame
ret, frame = cap.read()

if ret:
    # Save the frame to a file
    cv2.imwrite("captured_image.jpg", frame)
    print("Image saved to 'captured_image.jpg'")
else:
    print("Failed to capture image")

# Release the webcam
cap.release()