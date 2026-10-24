from tkinter import*
window=Tk()#This will create the window of the app
window.geometry("600x600")#It is defining the width and height of the window
window.title("Temperature Convertor")
window.config(background="gray")
heading=Label(window,text="Celsius to Farenheit Convertor",bg="gray",font=("Ariel",20))
heading.place(x=15,y=15)

def convertor1():
    celsius=int(Ent_entry.get())
    farenheit=(celsius*1.8)+32
    Result.config(text="Temperature in farenheit is:"+str(farenheit))











Ent=Label(window,text="Enter the temperature in celsius", bg="gray",fg="black",font=("Ariel",20))
Ent.place(x=15,y=250)
Ent_entry=Entry(window,width=10,font=("Ariel"))
Ent_entry.place(x=450,y=260)


Result=Label(window,)
Result.place(x=250,y=490)

convert_button1=Button(window,text="Convert to Farenheit",command=convertor1)
convert_button1.place(x=250,y=550)








window.mainloop()