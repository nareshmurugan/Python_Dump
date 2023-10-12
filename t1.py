'''
import turtle

t = turtle.Turtle()

t.up()
t.backward(400)
t.left(90)
t.down()
t.forward(250)
t.right(90)
t.forward(62.5)
t.backward(62.5 * 2)
t.forward(62.5)
t.right(90)
t.forward(250)
t.right(90)
t.forward(62.5)
t.backward(62.5 * 2)
t.up()
t.backward(100)
t.right(90)
t.down()
t.forward(250)
for x in range(180):
    t.forward(1)
    t.right(1)
####    
import turtle
turtle.setup(900,400)
wn = turtle.Screen()
wn.title("Turtle writing my name: IDAN")
wn.bgcolor("lightgreen")
turtle.width(30)
# turtle.pensize(30)

t = turtle.Turtle()
t.up()
t.backward(360)
t.left(90)
t.backward(80)
t.down()
t.forward(250)
t.right(90)
t.forward(62.5)
t.backward(62.5 * 2)
t.forward(62.5)
t.right(90)
t.forward(250)
t.right(90)
t.forward(62.5)
t.backward(62.5 * 2)
t.up()
t.backward(100)
t.right(90)
t.down()
t.forward(250)
t.right(90)
for x in range(180):
    t.right(1)
t.up()
t.right(90)
t.forward(230)
t.right(90)
t.forward(4*62.5)
t.right(65)
t.down()
t.forward(250)
t.right(180)
t.forward(275)
t.left(135)
t.forward(250)
t.right(180)
t.forward(120)
t.right(70)
t.forward(110)
t.right(90)
t.up()
t.forward(115)
t.left(90)
t.forward(1.5*62.5)
t.left(90)
t.down()
t.forward(250)
t.right(145)
t.forward(320)
t.left(145)
t.forward(250)

wn.mainloop()

'''
from turtle import Turtle, Screen

NAME = "IDAN"

BORDER = 1
BOX_WIDTH, BOX_HEIGHT = 10, 10  # letter bounding box
WIDTH, HEIGHT = BOX_WIDTH - BORDER * 2, BOX_HEIGHT - BORDER * 2  # letter size

def letter_A(turtle):
    turtle.forward(HEIGHT / 2)
    for _ in range(3):
        turtle.forward(HEIGHT / 2)
        turtle.right(90)
        turtle.forward(WIDTH)
        turtle.right(90)
    turtle.forward(HEIGHT)

def letter_D(turtle):
    turtle.forward(HEIGHT)
    turtle.right(90)
    turtle.circle(-HEIGHT / 2, 180, 30)

def letter_I(turtle):
    turtle.right(90)
    turtle.forward(WIDTH)
    turtle.backward(WIDTH / 2)
    turtle.left(90)
    turtle.forward(HEIGHT)
    turtle.right(90)
    turtle.backward(WIDTH / 2)
    turtle.forward(WIDTH)

def letter_N(turtle):
    turtle.forward(HEIGHT)
    turtle.goto(turtle.xcor() + WIDTH, BORDER)
    turtle.forward(HEIGHT)

LETTERS = {'A': letter_A, 'D': letter_D, 'I': letter_I, 'N': letter_N}

wn = Screen()
wn.setup(800, 400)  # arbitrary
wn.title("Turtle writing my name: {}".format(NAME))
wn.setworldcoordinates(0, 0, BOX_WIDTH * len(NAME), BOX_HEIGHT)

marker = Turtle()

for counter, letter in enumerate(NAME):
    marker.penup()
    marker.goto(counter * BOX_WIDTH + BORDER, BORDER)
    marker.setheading(90)

    if letter in LETTERS:
        marker.pendown()
        LETTERS[letter](marker)

marker.hideturtle()

wn.mainloop()

