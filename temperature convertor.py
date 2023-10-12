from tkinter import *
import tkinter
def fahcel():
    d=Entry.get(E1)
    c=Entry.get(E2)
    d=int(d)
    c=(c)
    if c =="1":
        answer = (d-32)*5/9
    if c =="2":
        answer = (d*9/5)+32
    Entry.insert(E3,1,answer)
    print(answer)

top=tkinter.Tk()
L1=Label(top, text="CALCULATOR FOR FAHRENHEIT <> CELSIUS",).grid(row=0,column=1)
L2=Label(top, text="ENTER THE DEGREE",).grid(row=1,column=0)
L3=Label(top, text="CHOOSE THE MEASUREMENT \nFOR FAHRENHEIT PRESS 1 or FOR CELSIUS PRESS 2 AND SUBMIT",).grid(row=2,column=0)
L4=Label(top, text="Answer",).grid(row=3,column=0)
E1=Entry(top,bd=20)
E1.grid(row=1,column=1)
E2=Entry(top,bd=20)
E2.grid(row=2,column=1)
E3=Entry(top,bd=20)
E3.grid(row=3,column=1)
B=Button(top,text ="Submit",command = fahcel).grid(row=4,column=1,)
top.mainloop()
