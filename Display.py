### Import             ###
from tkinter import *
from datetime import datetime
import psutil
import threading

### Root Configuration ###
root = Tk()
root.configure(bg="black")
root.title("OBS Display")
#root.geometry("100x20")

### Widgets            ###
def Draw():
    w1 = Label(text=datetime.now().strftime("%H:%M:%S"), bg="black", fg="white")
    w2 = Label(text=str(psutil.cpu_percent())+" CPU", bg="black", fg="white")
    w3 = Label(text="Widget 3", bg="black", fg="white")
    w4 = Label(text="Widget 4", bg="black", fg="white")

    w1.config(font=("LCDMono",44))
    w2.config(font=("LCDMono",44))
    w3.config(font=("LCDMono",44))
    w4.config(font=("LCDMono",44))

    w1.config(width=10,height=5)
    w2.config(width=10,height=5)
    w3.config(width=10,height=5)
    w4.config(width=10,height=5)

    w1.grid(row=0,column=0)
    w2.grid(row=0,column=1)
    w3.grid(row=1,column=0)
    w4.grid(row=1,column=1)

def Refresher():
    Draw()
    threading.Timer(0.5,Refresher).start()

##########################
Refresher()
##########################
root.mainloop()
