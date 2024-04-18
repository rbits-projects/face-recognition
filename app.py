import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # Open the default camera

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen():
    """Video streaming generator function."""
    while True:
        ret, frame = camera.read()  # Read frame from the camera
        if not ret:
            break
        # Resize the frame
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        # Encode the frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        # Convert the frame to bytes
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
