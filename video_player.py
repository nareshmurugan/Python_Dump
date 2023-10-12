import cv2
import os
import random

path="C:/Users/ELCOT/Videos"
def load_video(path):
    vid=[]
    for filename in os.listdir(path):
        if filename.endswith(".mp4"):
            vid.append(os.path.join(path,filename))
    return vid
vid=load_video(path)
vidnum=random.randrange(0,len(vid))
cap=cv2.VideoCapture(vid[vidnum])
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        cv2.imshow('frame',frame)
        if cv2.waitKey(25)==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
