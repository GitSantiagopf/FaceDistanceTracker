import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

class DistanceCamera:
    def __init__(self):
        self.detector = FaceMeshDetector(maxFaces=1)
        self.W = 6.3  # ancho real entre los puntos en centímetros
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not self.cap.isOpened():
            raise ValueError("No se pudo abrir la cámara. Asegúrate de que esté conectada correctamente.")

    def get_frames(self):
        while True:
            ret, frame = self.cap.read()  # Lee el fotograma de la cámara

            if not ret:  # Verifica si se capturó el fotograma correctamente
                print("No se pudo capturar el fotograma")
                break

            frame, faces = self.detector.findFaceMesh(frame, draw=False)

            if faces:
                face = faces[0]
                pointLeft = face[145]
                pointRight = face[374]

                # Calcula la distancia entre los puntos y la profundidad
                w, _ = self.detector.findDistance(pointLeft, pointRight)
                f = 570
                d = (self.W * f) / w  # Calcula la nueva distancia usando la longitud focal

                cvzone.putTextRect(frame, f'Distancia: {round(d,1)}cm', (face[10][0]-125, face[10][1]-50),colorT=(255, 255, 255), 
                           colorR=(255, 0, 0), scale = 2)
                
                yield frame

    def __del__(self):
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()  # Libera la cámara

