
from tkinter import*

window=Tk()
window.geometry("600x600")
window.title("Weight Convertor")
window.config(background="gray")

heading=Label(window,text="Weight Convertor",bg="gray",font=("Ariel",20))
heading.place(x=15,y=15)


# Kilograms to Grams
def convertor1():
    kg=float(Ent_entry.get())
    grams=kg*1000
    Result.config(text="Weight in grams is:"+str(grams))


# Grams to Kilograms
def convertor2():
    grams=float(Ent_entry2.get())
    kg=grams/1000
    Result2.config(text="Weight in kilograms is:"+str(kg))


# First converter
Ent=Label(window,text="Enter weight in kilograms",bg="gray",fg="black",font=("Ariel",15))
Ent.place(x=15,y=150)

Ent_entry=Entry(window,width=10,font=("Ariel"))
Ent_entry.place(x=400,y=155)

Result=Label(window,bg="gray")
Result.place(x=150,y=220)

convert_button1=Button(window,text="Convert to Grams",command=convertor1)
convert_button1.place(x=250,y=260)


# Second converter
Ent2=Label(window,text="Enter weight in grams",bg="gray",fg="black",font=("Ariel",15))
Ent2.place(x=15,y=350)

Ent_entry2=Entry(window,width=10,font=("Ariel"))
Ent_entry2.place(x=400,y=355)

Result2=Label(window,bg="gray")
Result2.place(x=150,y=420)

convert_button2=Button(window,text="Convert to Kilograms",command=convertor2)
convert_button2.place(x=250,y=470)


window.mainloop()
