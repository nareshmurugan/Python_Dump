import turtle
t=turtle.Turtle()
s=t.getscreen()
colors=["red","orange","yellow","green","blue","purple","black"]

for each_color in colors:
    angle=360/len(colors)
    t.color(each_color)
    t.circle(50)
    t.right(angle)
    t.backward(10)
