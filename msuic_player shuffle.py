import pygame
import os
import random
pygame.mixer.init()
path=("D:/my songs")
num=1
ismuted=0
ispaused=0
getbusy=0
def load_songs(path):
    songs=[]
    for filename in os.listdir(path):
        if filename.endswith(".mp3"):
            songs.append(os.path.join(path,filename))
    return songs
songs=load_songs(path)
for i in range(len(songs)):
    songnum=random.randrange(0,len(songs))
    pygame.mixer.music.load(songs[songnum])
    pygame.mixer.music.play()




