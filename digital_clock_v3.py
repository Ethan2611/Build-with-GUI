from tkinter import *#it is the graphical library of python
import datetime
from time import strftime
window=Tk()#This will create the window of the app
window.geometry("600x600")#It is defining the width and height of the window
window.title("Digital Clock")
window.config(background="light blue")
def time():#updates the clock each second
    currenttime=strftime('%I:%M:%S:%p')#this is the format of the time
    clock.config(text=currenttime)#shows the live time
    clock.after(1000,time)#updates the time every second


def date():#updates the date each day
    mydate=strftime('%d:%B:%Y')
    date1.config(text=mydate)



def day():
    myday=strftime('%A')
    day1.config(text=myday)







heading=Label(window,text="Digital Clock",bg="light blue",font=("Ariel",30))
heading.place(x=180,y=25)

clock=Label(window,bg="light blue",font=("Ariel",55))
clock.place(x=105,y=150)


date1=Label(window,bg="light blue",font=("Ariel",40))
date1.place(x=95,y=250)


day1=Label(window,bg="light blue",font=("Ariel",40))
day1.place(x=155,y=335)


time()
date()
day()














window.mainloop()
