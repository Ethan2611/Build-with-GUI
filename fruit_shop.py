from tkinter import * 
window=Tk()#This will create the window of the app
window.geometry("600x600")#It is defining the width and height of the window
window.title("Spinboxes")
window.config(background="light blue")
heading=Label(window,text="Fruitz App", bg="orange",fg="black",font=("Ariel",20))
heading.place(x=15,y=15)

def calculate_price():
    price=2
    fruit=fruits.get()
    quantity=int(numbers.get())
    tot_price=price*quantity
    total.config(text="the total price is:"+ str(tot_price))


fruits_message=Label(window,text="Please select the fruit you want",bg="light blue",fg="black",font=("Ariel",10))
fruits_message.place(x=15,y=230)
fruits=Spinbox(window,values=("Apple","Banana","Orange","Mango","Pineapple","Guava","Grapes","Dragon Fruit"))
fruits.place(x=15,y=250)



welcome=Label(window,text="Fruits and Vegetables are the colourful buidling blocks of a healthy life",font=("Ariel",10))
welcome.place(x=190,y=100)




numbers_message=Label(window,text="Please select the quantity of fruits you want",bg="light blue",fg="black",font=("Ariel",10))
numbers_message.place(x=20,y=155)
numbers=Spinbox(window,from_=0,to=10)
numbers.place(x=20,y=175)


calc_price=Button(window,text="Calculate Price",command=calculate_price)
calc_price.place(x=20,y=400)




total=Label(window,text="Total Price=",font=("Ariel",10))
total.place(x=400,y=500)
















window.mainloop()#To make the output window stay on the screen