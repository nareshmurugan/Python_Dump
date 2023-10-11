import pygame as pg# importing a module named pygame in python which was specialy made for deal with gaming
import random #it is module like pygame but it deals with random generator in python
import math #it is a module used to use the mathematical functions
from pygame import mixer

#intialize the pygame
pg.init() #'module name'.init() refers to call the all function we want in that module for the game

#creating a game window
screen = pg.display.set_mode((800,600)) #screen is default keyword in python pygame module it is used for creating a window and size of it
                                        #pg.dispay is a sub-module which had the set_mode function
#background
background = pg.image.load("p/bgp.jpg") #like screen it is also a keyword in module used to set bg

#background music                                        #image is sub-module of pygame which had the function load which help to read the image file 
mixer.music.load("p/Interstellar Main Theme - Extra Extended - Soundtr(MP3_160K).mp3 ")
mixer.music.play(-1)

#title and icons
pg.display.set_caption("SPACE INVADER") #with the help of fuction set_caption from pygame we set the name of the game as title
icon=pg.image.load("p/spaceship.png") #icon is a user-defind keyword here note it was used to set the icon of the tab 
pg.display.set_icon(icon) # set_icon is function used to set the icon *please ensure that icon is a picture is png file 
                          # inserted the user-defind keyword her to icon as icon  
#player( X axis = playerX , Y axis =PlayerY , the functional axis = playerX_change)
playerImg=pg.image.load('p/jet 2.png') # the image of the player was loading 
playerX=370 # the co-ordinate of the player is to be center we already done the screen size
playerY=480 # as 800,600 so the centre of it will be 480,370
playerX_change=0 # in game we dont want to change the y co-ordinate of the player as spaceship

#Enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyImg.append(pg.image.load('p/space-ship.png'))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)

#bullet
#ready you cant see the bullet on screen
#and fire the bullet is currtly moving
bulletImg=pg.image.load('p/bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

#score

score_value=0
font=pg.font.Font('freesansbold.ttf',32)

textX=10
textY=10

#game over text
over_font=pg.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))

    
def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x,y))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+(math.pow(enemyY-bulletY,2)))
    if distance <27:
        return True
    else:
        return False

        
#Gameloop
running=True
while running:
     #rgb=red green blue
    screen.fill((0,0,0))
    #background images
    screen.blit(background,(0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False

    # if keystroke is pressed check whether its right or left
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_a:
                playerX_change=-5
            if event.key==pg.K_l:
                playerX_change=5
            if event.key==pg.K_SPACE:
                    bullet_sound=mixer.Sound("p/Danganronpa Bullet Sound(MP3_160K).wav")
                    bullet_sound.play()
                    if bullet_state == "ready":
                        bulletX=playerX
                        fire_bullet(playerX,bulletY)
        if event.type==pg.KEYUP:
            if event.key==pg.K_a or event.key == pg.K_a:
                playerX_change=0

    
#boundary  creating for player
    playerX+=playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
        
#boundary  creating of enemy
    for i in range(num_of_enemies):
        #game over
        if enemyY[i]>480:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break


        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<= 0:
            enemyX_change[i]=2
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-2
            enemyY[i]+=enemyY_change[i]
            
        #collision
        collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound=mixer.Sound('p/THE Boom   Sound Effect(MP3_160K).wav')
            explosion_sound.play()
            bulletY=480
            bullet_state="ready"
            score_value+=1
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)
         
            
        enemy(enemyX[i],enemyY[i],i)
        
#bullet movement
    if bulletY <=0:
        bulletY=480
        bullet_state='ready'
        
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    player(playerX,playerY)
    show_score(textX,textY)
    pg.display.update()

