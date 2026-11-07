from tkinter import *#it is the graphical library of python
import datetime
from time import strftime
window=Tk()#This will create the window of the app
window.geometry("600x600")#It is defining the width and height of the window
window.title("Digital Clock")
window.config(background="light blue")
def time():#updates the clock each second
    currenttime=strftime('%H:%M:%S:%p')#this is the format of the time
    clock.config(text=currenttime)#shows the live time
    clock.after(1000,time)#updates the time every second









heading=Label(window,text="Digital Clock",bg="light blue",font=("Ariel",30))
heading.place(x=180,y=25)

clock=Label(window,bg="light blue",font=("Ariel",55))
clock.place(x=105,y=150)

time()















window.mainloop()
