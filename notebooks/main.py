import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = FaceMeshDetector(maxFaces=1)

textList = ['Welcome to GitSantiagoPf.',
            'This is a', 'face distance estimator',
            'Follow me for more.']

while True:
    ret, img = cap.read()
    imgText = np.zeros_like(img)
    img, faces = detector.findFaceMesh(img, draw=False)
    
    if faces:
        face = faces[0]
        
        pointLeft = face[145]
        pointRight = face[374]
        
        #cv2.line(img, pointLeft, pointRight, (255, 255, 255), 3)
        
        #cv2.circle(img, pointLeft, 5, (255, 0, 0), cv2.FILLED)
        #cv2.circle(img, pointRight, 5, (255, 0, 0), cv2.FILLED)
        
        w, _ = detector.findDistance(pointLeft, pointRight)
        
        
        # Finding the Focal Length
        W = 6.3
        #d = 78       
        #f = (w*d)/W
        
        #print(f)
        
        f = 610
        # Finding distance
        d = (W*f)/w
        
        #print(d)
        
        cvzone.putTextRect(img, f'Distance: {round(d,1)}cm', (face[10][0]-125, face[10][1]-50),
                           scale = 2, colorR = (255,0,0))
        
        for i, text in enumerate(textList):
            singleHeight = 20 + int((int(d/10)*10)/4)
            scale = 0.4 + (int(d/10)*10) / 80
            cv2.putText(imgText, text, (50, 200 + (i * singleHeight)), cv2.FONT_HERSHEY_SIMPLEX, 
                scale, (255, 255, 255), 2)              
        
    imgStacked = cvzone.stackImages([img, imgText], 2, 1)            
    cv2.imshow('Image', imgStacked)
    cv2.waitKey(1)