import turtle
t=turtle.Turtle()
s=t.getscreen()
t.penup(),t.lt(90),t.fd(200),t.lt(245),t.bk(100),t.pendown()
t.begin_fill()
t.pen(pencolor='gold',fillcolor='white',pensize=10,speed=5000)
t.rt(90),t.fd(100),t.penup(),t.lt(90),t.fd(50),t.lt(90),t.pendown(),t.fd(100),t.penup,
t.bk(50),t.lt(90),t.pendown(),t.fd(50),t.penup(),t.bk(60),t.lt(90),t.fd(50),t.pendown()
t.lt(160),t.fd(100),t.rt(135),t.fd(100),t.penup(),t.bk(50),t.rt(90),t.pendown(),t.fd(50),
t.penup(),t.bk(55),t.rt(260),t.fd(60),t.pendown(),t.lt(145),t.fd(90),t.rt(90),t.fd(90),
t.rt(90),t.fd(45),t.rt(90),t.fd(50),t.bk(50),t.lt(90),t.penup(),t.fd(45),t.lt(180),t.fd(3),
t.fd(3),t.pendown(),t.fd(3)
t.fd(90),t.rt(90),t.fd(90),t.rt(90),t.fd(45),t.rt(90),t.fd(50),t.bk(50),t.lt(90),t.penup(),
t.fd(45),t.lt(90),t.fd(2)
t.lt(90),t.fd(40),t.lt(90),t.fd(45),t.lt(30),t.fd(55),t.bk(55),t.rt(60),t.fd(55),t.bk(55),
t.rt(150),t.fd(45),t.rt(90),t.fd(100)
t.rt(180),t.fd(50),t.rt(180),t.lt(90),t.penup(),t.fd(40),t.lt(90),t.pendown(),t.fd(45),
t.lt(30),t.fd(55),t.bk(55),t.rt(60),t.fd(55),t.bk(55),t.rt(150),t.fd(45),t.penup(),t.lt(90),
t.fd(50),t.rt(90),t.fd(300),t.rt(90),t.fd(400),t.rt(180)                                                   
t.pendown(),t.rt(245),t.fd(100),t.rt(90),t.fd(50),t.rt(90),t.fd(50),t.rt(90),t.fd(50),
t.penup(),t.bk(50),t.rt(90),t.fd(50),t.rt(90),t.fd(10),t.rt(90),t.penup(),t.fd(100),
t.rt(90),t.fd(3),t.rt(90),t.pendown(),t.fd(100),t.rt(90),t.fd(50),t.rt(90),t.fd(100),
t.rt(90),t.fd(50),t.bk(50),t.fd(3)
t.rt(180),t.fd(10),t.lt(90),t.fd(100),t.rt(150),t.fd(115),t.rt(210),t.fd(100),t.bk(100),
t.rt(90),t.penup(),t.fd(10)
t.pendown(),t.fd(90),t.lt(90),t.fd(50),t.lt(90),t.fd(25),t.bk(25),t.penup(),t.rt(90),t.fd(50),
t.pendown(),t.lt(90),t.fd(90),t.lt(90),t.fd(100),t.penup(),t.lt(90),t.fd(110)
t.pendown(),t.lt(65),t.fd(100),t.rt(130),t.fd(100),t.bk(50),t.rt(90),t.fd(60),t.bk(60),t.lt(90),
t.fd(50),t.lt(65),t.penup(),t.fd(10),t.pendown(),t.lt(90),t.fd(100),t.bk(100),t.rt(90),
t.fd(100)
t.penup(),t.lt(153),t.fd(450)
t.end_fill()
t.pendown()
colors=["red","orange","yellow","green","blue","purple","red"]
for each_color in colors:
    angle=360/len(colors)
    t.color(each_color)
    t.circle(50)
    t.right(angle)
    t.backward(10)



 
