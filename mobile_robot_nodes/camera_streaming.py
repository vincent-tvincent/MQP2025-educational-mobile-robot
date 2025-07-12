import cv2
from flask import Flask, Response

# Initialize the Flask app
app = Flask(__name__)

# Open the camera (0 is usually the default camera, you may need to change it if you have multiple cameras)
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
video_capture.set(cv2.CAP_PROP_GAIN, 1.0)  # Gain setting (0.0 to 1.0)
video_capture.set(cv2.CAP_PROP_EXPOSURE, -10)
# video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
# video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)
# Check if the camera opened correctly
if not video_capture.isOpened():
    print("Error: Could not open camera.")
    exit()

def generate_frames():
    while True:
        # Read the frame from the webcam
        success, frame = video_capture.read()

        # If reading the frame was successful
        if not success:
            break
        else:
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)

            # Convert the buffer to bytes
            frame = buffer.tobytes()

            # Yield the frame in the correct format for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return "Webcam streaming is active. Go to /video_feed to view the stream."

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
