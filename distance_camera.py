import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

class DistanceCamera:
    def __init__(self):
        self.detector = FaceMeshDetector(maxFaces=1)
        self.REAL_WIDTH = 6.3  # Real width between points in centimeters
        self.CAMERA_INDEX = 0
        self.cap = cv2.VideoCapture(self.CAMERA_INDEX, cv2.CAP_DSHOW)
        if not self.cap.isOpened():
            raise ValueError("Could not open the camera. Please ensure it is connected properly.")

    def get_frames(self):
        while True:
            ret, frame = self.cap.read()  # Read a frame from the camera

            if not ret:  # Check if the frame was captured correctly
                print("Failed to capture frame")
                break

            frame, faces = self.detector.findFaceMesh(frame, draw=False)

            if faces:
                face = faces[0]
                point_left = face[145]
                point_right = face[374]

                # Calculate the distance between points and the depth
                width_pixels, _ = self.detector.findDistance(point_left, point_right)
                focal_length = 570
                distance = (self.REAL_WIDTH * focal_length) / width_pixels  # Calculate the distance using the focal length

                cvzone.putTextRect(frame, f'Distance: {round(distance, 1)} cm', 
                                   (face[10][0] - 125, face[10][1] - 50), 
                                   colorT=(255, 255, 255), colorR=(255, 0, 0), scale=2)
                
                return frame

    def __del__(self):
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()  # Release the camera


