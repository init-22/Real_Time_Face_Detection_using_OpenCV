#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
from mtcnn.mtcnn import MTCNN
from math import sqrt
detector = MTCNN()

video_capture = cv2.VideoCapture("nasdaily.mp4")


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    #Use MTCNN to detect faces
    result = detector.detect_faces(frame)
    if result != []:
        for person in result:
            bounding_box = person['box']
   
            cv2.circle(frame, (bounding_box[0], bounding_box[1]), 80, (0, 0, 0), 2)


    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

