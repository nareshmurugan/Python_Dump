import cv2
import csv
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(minTrackCon=0.8)

class MCQ():
    def __init__(self,data):
        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.answer = int(data[5])

        self.userAns = None

    def update(self, cursor, bboxs):

        for x, bbox in enumerate(bboxs):
            x1,y1,x2,y2 = bbox
            if x1<cursor[0]<x2 and y1<cursor[1]<y2:
                self.userAns = x+1
                cv2.rectangle(img, (x1,y1), (x2,y2),(0,255,0), cv2.FILLED)



# Import csv file data
pathCSV = "Mcqs.csv"
with open(pathCSV,newline='\n') as f:
    reader = csv.reader(f)
    dataAll = list(reader)[1:]
# print(len(data))

# Create Object for each MCQ
mcqList = []
for q in dataAll:
    mcqList.append(MCQ(q))

print("Total MCQ objects Created:", len(mcqList))

qNo = 0
qTotal = len(dataAll)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if qNo<qTotal:
        mcq = mcqList[qNo]

        img, bbox = cvzone.putTextRect(img, mcq.question, [100, 50], 1, 1, offset=25, border=5)
        img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [100, 150], 1, 1, offset=25, border=5)
        img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [400, 150], 1, 1, offset=25, border=5)
        img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [100, 250], 1, 1, offset=25, border=5)
        img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [400, 250], 1, 1, offset=25, border=5)

        if hands:
            lmList = hands[0]['lmList']
            cursor = lmList[8]  # 8 is tip of index finger
            length, info = detector.findDistance(lmList[8],lmList[12])
            # print(length)
            if length < 30:
                # print("Clicked")
                mcq.update(cursor, [bbox1, bbox2, bbox3, bbox4])
                print(mcq.userAns)
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    qNo +=1

    else:
        score=0
        for mcq in mcqList:
            if mcq.answer == mcq.userAns:
                score += 1
        score = round((score/qTotal)*100,2)
        img, _ = cvzone.putTextRect(img, "Quiz Completed", [150, 100], 1, 1, offset=50, border=5)
        img, _ = cvzone.putTextRect(img, f'Your Score: {score}%', [400, 100], 1, 1, offset=50, border=5)

    """   
    # Draw Progress bar
    barvalue = 100 + (400//qTotal)*qNo
    cv2.rectangle(img, (100, 350), (500, 400), (0,255,0), cv2.FILLED)
    cv2.rectangle(img, (100, 350), (500, 400), (255, 0, 255), 5)
    """

    # Draw Progress bar
    barValue = 100 + (400 // qTotal) * qNo
    cv2.rectangle(img, (100, 350), (barValue, 400), (0, 255, 0), cv2.FILLED)
    cv2.rectangle(img, (100, 350), (500, 400), (255, 0, 255), 5)
    img, _ = cvzone.putTextRect(img, f'{round((qNo/qTotal)*100)}%', [540, 380], 2, 2, offset=16)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        cv2.destroyAllWindows()
        break

