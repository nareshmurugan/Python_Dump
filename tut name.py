import turtle,time
t=turtle.Turtle()
s=turtle.getscreen()
name=input("ENTER YOUR NAME").upper()
n=[]
for i in name:
    n.append(i)
ALPHA=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
t.hideturtle()
if(ALPHA[0]==n[0]):
    t.bk(500);t.lt(70);t.fd(100);t.rt(140);t.fd(100);t.bk(50);t.rt(110);t.fd(36);t.rt(180);t.fd(36);t.rt(70);t.fd(50);t.lt(70);t.fd(10);t.rt(90)
if(ALPHA[1]==n[1]):
    t.lt(180);t.fd(95);t.rt(90);t.fd(65);t.rt(90);t.fd(50);t.rt(90);t.fd(65);t.bk(65);t.lt(90);t.fd(45);t.rt(90);t.fd(70);t.bk(100);t.rt(90)
if(ALPHA[2]==n[2]):
    t.rt(360);t.fd(95);t.rt(90);t.fd(65);t.bk(65);t.lt(90);t.bk(95);t.rt(180)
