import speech_recognition as sr
r=sr.Recognizer()
with sr.AudioFile("D:/python/levitate.wav") as source:
    audio=r.record(source)
try:
    Text=r.recognize_google(audio)
    print("working on..........")
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))
