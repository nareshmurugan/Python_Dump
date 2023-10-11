import turtle as t
t=t.Turtle()
s=t.getscreen()
'''for i in range(20):
    t.lt(45)
    t.fd(90)
    t.lt(100)
    t.fd(90)
'''
colors=["red","orange","yellow","green","blue","purple","black"
        ,"red","orange","yellow","green","blue","purple",
        "red","orange","blue"]
i=1
a=45
b=90
c=100
while i<200:
    a+=1;c+=1;
    t.pen(pencolor="red",fillcolor="yellow",pensize=3,speed=5)
    t.begin_fill()
    t.lt(a)
    t.fd(b)
    t.lt(c)
    t.fd(b)
    t.end_fill()
    i+=1

while i<200:
    a+=1;c+=1;
    t.pen(pencolor="blue",fillcolor="green",pensize=3,speed=5)
    t.begin_fill()
    t.rt(a)
    t.fd(b)
    t.rt(c)
    t.fd(b)
    t.end_fill()
    i+=1

'''for i in range(20):#d1
    t.lt(45)
    t.fd(90)
    t.lt(100)
    t.fd(90)
for i in range(20):#d2
    t.lt(45)
    t.fd(90)
    t.lt(60)
    t.fd(90)
for i in range(20):#d3
    t.rt(45)
    t.fd(90)
    t.rt(60)
    t.fd(90)
''' 
time.speed(1000)    
    
