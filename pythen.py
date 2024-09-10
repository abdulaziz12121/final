import streamlit as st
import cv2
import tempfile
import os

# Streamlit app title
st.title("Video File Upload and Display")

# Allow user to upload a video file
uploaded_video = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov", "mkv"])

# Check if a video file is uploaded
if uploaded_video is not None:
    # Save uploaded file temporarily
    temp_file = tempfile.NamedTemporaryFile(delete=False) 
    temp_file.write(uploaded_video.read())
    
    # Display video using Streamlit
    st.video(uploaded_video)

    # Load video using OpenCV (Optional for further processing)
    video_capture = cv2.VideoCapture(temp_file.name)

    st.write("Processing video...")

    # Process video frames
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break
        
        # You can display frame-by-frame processing (Optional)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame for display in Streamlit
        # st.image(frame)  # Display each frame (optional)

    video_capture.release()
    os.remove(temp_file.name)  # Remove the temporary file when done
else:
    st.write("Please upload a video file.")
