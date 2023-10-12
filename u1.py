from gtts import gTTS
from playsound import playsound
audio='speech.mp3'
sp=gTTS(text="open your eyes sir",lang='en')
sp.save(audio)
playsound(audio)
