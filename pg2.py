import pygame as pg
#initialize pygame
pg.init()
screen=pg.display.set_mode((800,600))

#title and icon
pg.display.set_caption("f_i_s_h_fan_a_t_i_c_s")
icon=pg.image.load('D:/flying-fish.png')
pg.display.set_icon(icon)
#screen runing
running =True
#player
playerImg=pg.image.load('D:/please.png')
playerX=370
playerY=480

def player(x,y):
    screen.blit(playerImg,(x,y))
#game loop
while running:
    screen.fill((0,0,0))
    playerY-=.1
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
            
    player(playerX,playerY)
    pg.display.update()

