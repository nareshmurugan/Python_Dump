import speech_recognition as SRG 
import time
import os

store = SRG.Recognizer()
with SRG.Microphone() as s:
     
    print("Speak...")
     
    audio_input = store.record(s, duration=7)
    print("Recording time:",time.strftime("%I:%M:%S"))
    
    try:
        text_output = store.recognize_google(audio_input)
        print("Text converted from audio:\n")
        print(text_output)
        print("Finished!!")
 
        print("Execution time:",time.strftime("%I:%M:%S"))
    except:
           print("Couldn't process the audio input.")
text=text_output.split()[-1]
os.chdir(f'C:/Users/ELCOT/Desktop/{text}')
os.system("manim scene.py -pql")

