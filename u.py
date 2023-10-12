from gtts import gTTS
from playsound import playsound
audio1='wake.mp3'
sp=gTTS(text="wake up sirr ",lang='en')
playsound(audio1)
