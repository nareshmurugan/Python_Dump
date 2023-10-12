import turtle

#Takes user input to decide how many squares are needed
f=int(input("How many squares do you want?"))
c=int(input("What colour would you like? red = 1, blue = 2 and green =3"))
n=int(input("What background colour would you like? red = 1, blue = 2 and green =3"))

i=1

x=360

#Draws the desired number of squares.
while i < f:
    i=i+1
    x=x*1.05
    print ("minimise this window ASAP")
    if c==1:
        turtle.pencolor("red")
    elif c==2:
        turtle.pencolor("blue")
    elif c==3:
        turtle.pencolor("green")
    else:
        turtle.pencolor("black")
    if n==1:
        turtle.fillcolor("red")
    elif n==2:
        turtle.fillcolor("blue")
    elif n==3:
        turtle.fillcolor("green")
    else:
        turtle.fillcolor("white")
    turtle.bk(x)
    turtle.rt(90)
    turtle.bk(x)
    turtle.rt(90)
    turtle.bk(x)
    turtle.rt(90)
    turtle.bk(x)
    turtle.rt(90)
    turtle.up()
    turtle.rt(9)
    turtle.down()
