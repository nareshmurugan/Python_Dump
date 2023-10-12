from pygame import mixer
mixer.init()
songs=["D:\my songs\Enthiran-320kbps-MassTamilan.com\Arima-Arima.mp3",
       "D:\my songs\Enthiran-320kbps-MassTamilan.com\Boom-Boom-Robo-Da.mp3",
       "D:\my songs\Enthiran-320kbps-MassTamilan.com\Chitti-Dance-Showcase.mp3",
       "D:\my songs\Enthiran-320kbps-MassTamilan.com\Irumbile-Oru-Idhaiyam.mp3",
       "D:\my songs\Enthiran-320kbps-MassTamilan.com\Kadal-Anukkal.mp3",
       "D:\my songs\Enthiran-320kbps-MassTamilan.com\Kilimanjaro.mp3",
       "D:\my songs\Enthiran-320kbps-MassTamilan.com\Puthiya-Manidha.mp3"]
for i in songs:
    mixer.music.load(i)
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
    
