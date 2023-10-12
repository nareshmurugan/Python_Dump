import pygame
import os
import random
pygame.mixer.init()
path=("D:/my songs")
num=1
ismuted=0
ispaused=0
get_busy=0
def load_songs(path):
    songs=[]
    for filename in os.listdir(path):
        if filename.endswith(".mp3"):
            songs.append(os.path.join(path,filename))
    return songs
songs=load_songs(path)
songnum=random.randrange(0,len(songs))
pygame.mixer.music.load(songs[songnum])

while(num!=0):
    print("1. play 2. pause 3.stop 4. resume 5. mute 6. unmute7. max sound 8. decrease sound 9. play next song 0. exit")
    print("enter your choice number")
    num=input()
    if num=='1':
        pygame.mixer.music.play()
    elif num=='2':
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            ispaused=1
        else:
            print("the player is not runing")
    elif num=='4':
        if ispaused:
            pygame.mixer.music.unpause()
            print("the song is resumed")
        else:
            print("the song is not paused")
    elif num=='3':
        pygame.mixer.music.stop()
    elif num=='5':
        earlierVolume=pygame.mixer.music.set_volume()
        pygame.mixer.music.set_volume(0)
    elif num=='6':
        pygame.mixer.music.set_volume(earlierVolume)
    elif num=='7':
        pygame.mixer.music.set_volume(1)
    elif num=='8':
        pygame.mixer.music.set_volume(0.25)
    elif num=='9':
        while 1:
            if(not pygame.mixer.music.get_busy()):
                songnum=random.randrange(0,len(songs))
                pygame.mixer.music.load(songs[songnum])
                pygame.mixer.music.play()                    
    elif num=='0':
        pygame.mixer.quit()
        break
    else:
        print("please enter valid number")  

