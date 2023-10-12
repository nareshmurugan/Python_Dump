#import turtle turtle and time module
import turtle,time
#initializing turtle module
python_hub = turtle.Turtle()
#assigning shape as turtle
python_hub.shape('turtle')
python_hub.shapesize(1)
#creating a list with colors
colors=["red","orange","yellow","green","blue","purple","black"]
#creating circles with each color
for each_color in colors:
    angle=360/len(colors)
    python_hub.color(each_color)
    python_hub.circle(40)
    python_hub.right(angle)
    python_hub.forward(30)
#using time.sleep()
time.sleep(10)
