from pycon import *
def setup():
    global displayWidth,displayHeight
    size(displayWidth/2,displayHeight)
    background(0)
def draw():
    beginShape()
    vertex(50,100)
    vertex(200,300)
    vertex(400,300)
    vertex(500,50)
    endShape()
