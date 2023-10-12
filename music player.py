from pygame import mixer
mixer.init()
mixer.music.load("D:/my songs/Azhaipaya-MassTamilan.org.mp3")
mixer.music.set_volume(9.0)
mixer.music.play()
while True:
    print("press 'p' to pause 'r' to resume")
    print("press 'e' to exit the program")
    query=input(">>>")
    if query =='p':
        mixer.music.pause()
    elif query =='r':
        mixer.music.unpause()
    elif query =='e':
        mixer.music.stop()
        break
