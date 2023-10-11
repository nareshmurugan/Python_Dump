import cv2 # to use opencv function and atributes 
import numpy as np # to use numpy array to find the differences
import mediapipe as mp # to use the straight line showing functionality through
                       # the camera to show as 
import autopy          # it the module we are using to operate the mouse access
import time            # it is a module to work with time  
import HandTrackingModule as htm   # it is module created by user defind in programme

#################
wCam,hCam=640,480 #wCam is width of the screen & hCam is the height of the screen 
#################
wScr,hScr=autopy.screen.size()
print(wScr,hScr)
cap=cv2.VideoCapture(0)#to use the camera as the input by VideoCapture() method of cv2
cap.set(3,wCam) # assigning the screen  
cap.set(4,hCam)  #size to the output by the set method set()
pTime=0 # previous time to run frame rate
detector=htm.handDetector(maxHands=1) #here htm is the handtracking module and 
# detector is the object to access the handdectector function attributes
while True:
     # 1. find hand landmarks
    success, img =cap.read()  #to get the picture from the video at loop
                                # success and img is the variable to store
                                  # the current picture or Frame while running
                                    # loop for infinitly
    img=detector.findHands(img) #img is the object to store the hand shape per frame
    lmList,bbox=detector.findPosition(img)# lmlist is to store the hand positions
                                # in the frame per second and bbox is bounding box
    
    
    # 2. get the tip of middle and index finger
    if len(lmList)!=0:
        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:]
        #print(x1,y1,x2,y2)
    # 3. check which finger are up
        fingers=detector.fingersUp()
        print(fingers)
    # 4. Only index finger: Moving mode
        
    # 5. Convert Coordinates
        if fingers[1]==1 and fingers[2]==0:
            x3=np.interp(x1,(0,wCam),(0,wScr))
            y3=np.interp(y1,(0,hCam),(0,hScr))
    # 6. Smoothen values
    # 7. Move Mouse
            autopy.mouse.move(x3,y3)
    # 8. If both Middle and Index fingers are up: Clicking mode
    # 9. Find distance between two fingers
    # 10. Clicking mouse if distance is short may be a touch of two
    # 11. Frame rate
    cTime=time.time()
    fps=1/(cTime-pTime)
    cv2.putText(img, str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)         
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    
