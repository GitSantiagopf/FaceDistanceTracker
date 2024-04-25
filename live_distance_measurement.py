import cv2
import streamlit as st
import numpy as np
from distance_camera import DistanceCamera

# Function to apply custom CSS styles
def load_custom_css(file_name):
    with open(file_name) as file:
        st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

# Load custom CSS styles
load_custom_css('styles.css')

# Application title and description
st.title('Real-Time Distance Camera')
st.write('This application captures real-time video and calculates the distance between the face and the camera.')

# Create an instance of the DistanceCamera class
distance_camera = DistanceCamera()

# Placeholder for displaying the video
frame_placeholder = st.empty()

# Initialize the capture state
if 'capture_active' not in st.session_state:
    st.session_state['capture_active'] = True

# Placeholder for the stopped capture message
message_placeholder = st.empty()

# Update buttons based on the current state
button_placeholder = st.empty()
if st.session_state['capture_active']:
    if button_placeholder.button('Stop Capture'):
        st.session_state['capture_active'] = False
        message_placeholder.write('Capture stopped. Press "Start Capture" to continue.')
        st.experimental_rerun()  # Force an immediate rerun of the script
else:
    if button_placeholder.button('Start Capture'):
        st.session_state['capture_active'] = True
        message_placeholder.empty()  # Clear the message when capture restarts
        st.experimental_rerun()  # Force an immediate rerun of the script

# Main loop to capture and display the video
if st.session_state['capture_active']:
    while distance_camera.cap.isOpened():
        frame = distance_camera.get_frames()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels='RGB')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
else:
    message_placeholder.write('Capture stopped. Press "Start Capture" to continue.')
    distance_camera.__del__()  # Properly release the camera

# Cleanup resources at the end
del distance_camera
cv2.destroyAllWindows()

