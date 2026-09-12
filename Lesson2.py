from tkinter import *#it is the graphical library of python
window=Tk()#This will create the window of the app
window.geometry("600x600")#It is defining the width and height of the window
window.title("Athletics Academy Form")
window.config(background="red")

heading=Label(window,text="Athletics Academy Application Form",bg="red",fg="black",font=("Ariel",20))
heading.place(x=15,y=15)
Name=Label(window,text="Enter the Child's Name",bg="red",fg="black",font=("Ariel",20))
Name.place(x=15,y=175)
name_entry=Entry(window,width=30,font=("Ariel"))
name_entry.place(x=300,y=185)

Age=Label(window,text="Enter the Child's Age", bg="red",fg="black",font=("Ariel",20))
Age.place(x=15,y=250)
Age_entry=Entry(window,width=10,font=("Ariel"))
Age_entry.place(x=300,y=260)

Mobile=Label(window,text="Enter Your Mobile Number",bg="red",fg="black",font=("Ariel",20))
Mobile.place(x=15,y=325)
Mobile_entry=Entry(window,width=10,font=("Ariel"))
Mobile_entry.place(x=360,y=335)

experience=Label(window,text="Child's Sports History",bg="red",fg="black",font=("Ariel",20))
experience.place(x=15,y=400)
experience_entry=Entry(window,width=20,font=("Ariel"))
experience_entry.place(x=300,y=410)

submit_button=Button(window,text="Submit",command=window.destroy)
submit_button.place(x=300,y=550)

window.mainloop()#To make the output window stay on the screen
