#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import face_recognition
from math import sqrt

# Get a reference to video
video_capture = cv2.VideoCapture("nasdaily.mp4")

# Initialize variables
face_locations = []

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        # Draw a box around the face
        one = int((left+right)/2)
        two = int((top+bottom)/2)
        radius = int(sqrt(top+bottom+left+right))
        cv2.circle(frame, (one, two), radius+30, (0, 0, 0), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

