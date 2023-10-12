import turtle,time
t=turtle.Turtle()
s=t.getscreen()
t.begin_fill()
t.pen(pencolor='black',fillcolor='red',pensize=3,speed=5)
t.begin_fill()
for i in range(3):
    t.fd(200);t.lt(120);t.fd(200);t.lt(120);t.fd(200)
    i+=1
t.end_fill()
t.pen(pencolor='black',fillcolor='green',pensize=3,speed=5)
t.begin_fill()
for i in range(3):
    t.rt(120);t.fd(200);t.lt(120);t.fd(200);t.lt(120);t.fd(200)
    i+=1
t.end_fill()
t.pen(pencolor='black',fillcolor='blue',pensize=3,speed=5)
t.begin_fill()
for i in range(3):
    t.rt(120);t.fd(200);t.lt(120);t.fd(200);t.lt(120);t.fd(200)
    i+=1
t.end_fill()
t.shape('triangle')
#creating a list with colors
colors=["red","orange","yellow","green","blue","purple","black"]

for each_color in colors:
    angle=360/len(colors)
    t.color(each_color)
    t.circle(100)
    t.right(angle)
    t.backward(1)
#using time.sleep()
time.sleep(100)




