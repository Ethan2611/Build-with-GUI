from tkinter import * 
window=Tk()#This will create the window of the app
window.geometry("600x600")#It is defining the width and height of the window
window.title("Spinboxes")
window.config(background="cyan")
heading=Label(window,text="Spinbox", bg="cyan",fg="black",font=("Ariel",20))
heading.place(x=15,y=15)
colors=Spinbox(window,values=("Red","Blue","Yellow","Green","Purple","Orange","Brown","Pink"))
colors.place(x=15,y=250)



numbers=Spinbox(window,from_=0,to=10)
numbers.place(x=20,y=175)


















window.mainloop()#To make the output window stay on the screen