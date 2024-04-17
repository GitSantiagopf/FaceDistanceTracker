import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(1)

while True:
    succes, img = cap.read()
    cv2.imshow('Image', img)
    cv2.waitKey(1)