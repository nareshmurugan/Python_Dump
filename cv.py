import cv2 as cv
img=cv.imread('C://Users//ELCOT//AppData//Local//Programs//Python//Python38//b.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)
