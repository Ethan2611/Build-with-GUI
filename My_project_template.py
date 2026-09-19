from tkinter import *#it is the graphical library of python
window=Tk()#This will create the window of the app
window.geometry("600x600")#It is defining the width and height of the window
window.title("Project")
window.config(background="red")

heading=Label(window,text="Project Details",bg="red",fg="black",font=("Ariel",20))
heading.place(x=15,y=15)



Pick_Template=Label(window,text="Pick a template",bg="red",fg="black",font=("Ariel",20))
Pick_Template.place(x=15,y=175)
Pick_Template_entry=Entry(window,width=30,font=("Ariel"))
Pick_Template_entry.place(x=300,y=185)


Name_project=Label(window,text="Name your Project", bg="red",fg="black",font=("Ariel",20))
Name_project.place(x=15,y=250)
Name_project_entry=Entry(window,width=10,font=("Ariel"))
Name_project_entry.place(x=300,y=260)

submit_button=Button(window,text="Create Project",command=window.destroy)
submit_button.place(x=300,y=550)

window.mainloop()#To make the output window stay on the screen
