import pygame as pg
pg.init()
screen=pg.display.set_mode((1366,768))
done=False
is_blue=True
x=30
y=30
clock=pg.time.Clock()
while not done:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            done=True
        if event.type==pg.KEYDOWN and event.key==pg.K_SPACE:
            is_blue=not is_blue
    pressed = pg.key.get_pressed()
    if pressed [pg.K_UP]:y-=3
    if pressed [pg.K_DOWN]:y+=3
    if pressed [pg.K_LEFT]:x-=3
    if pressed [pg.K_RIGHT]:x+=3
    screen.fill((0,0,0))
    if is_blue:
        color=(0,128,255)
    else:
        color=(255,100,0)
    pg.draw.rect(screen,color,pg.Rect(x,y,60,60))
    pg.display.flip()
    clock.tick(60)  
