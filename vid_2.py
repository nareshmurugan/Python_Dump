import cv2
import numpy as np
import dlib

#connects ti your computer's default camera
cap=cv2.VideoCapture(0)
#detect the coordinates
detect=dlib.get_frontal_face_dector()

#capature frames continously

while True:
    #capture frame-by-frame
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    #Rbg to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=detector(gray)
# itreate to count face
    i=0
    for face in faces:
        # get the coordinates at faces
        x,y=face.left(),face.top()
        x1,y1=face.right(),face.bottom()
        cv2.rectangle(frame,(x,y),(x1,y1),(0,255,0),2)
        # increment uteratir fir each face in faces
        i+=1
        # display the box and face
        cv2.putText(frame,'face num'+str(i),(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        print(face,i)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    # This command let's us quit with the 'q' button on a keyboard
    if cv2.waitkey(1)&0xFF ==ord('q'):
        break

# Release the capture and destroy the windows
cap.release()
cv2.destriyAllWindows()
