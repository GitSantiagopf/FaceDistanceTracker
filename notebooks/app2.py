import cv2 
import streamlit as st
import numpy as np
import tempfile
from DistanceCamera import DistanceCamera

distance_camera = DistanceCamera()

st.title('VideoCapture')

frame_placeholder = st.empty()

stop_button_pressed = st.button('Stop')

while distance_camera.cap.isOpened() and not stop_button_pressed:
     
     frame = distance_camera.get_frames()
     
     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
     frame_placeholder.image(frame, channels='RGB')
     
     if cv2.waitKey(1) & 0xFF == ord('q') or stop_button_pressed:
          break
     

del distance_camera  # Limpia y libera recursos al finalizar
st.write('Capture ended')
cv2.destroyAllWindows()