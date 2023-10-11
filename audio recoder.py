import sounddevice as sd
import soundfile as sf
from tkinter import *

def voice_rec():
    #seconds
    duration=5
    myrecording=sd.rec(int(duration * fs),sanplerate=fs, channels=2)
    sd.wait()
    #save as flac file at correct sampling rate return sf.write("my_auto_file.flac',amurecording,fs)
master=Tk()
Label(master,text="Voice Recoder:").grid(row=0,sticky=W,rowspan=5)
b=Button(master,text="Start",command=voice_rec)
b.grid(row=0,column=2,columnspan=2,rowspan=2,padx=5,pady=5)
mainloop()
