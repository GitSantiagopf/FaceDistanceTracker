from flask import Flask
from flask import render_template
from flask import Response
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from DistanceCamera import DistanceCamera


app = Flask(__name__)

def generate(camera):
    for frame in camera.get_frames():
        ret, encoded_frame = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_frame) + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    camera = DistanceCamera()
    return Response(generate(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, port = 5001)