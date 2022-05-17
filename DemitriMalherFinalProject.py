from cProfile import label
from cgitb import text
from optparse import Option
from random import random
from select import select
from tkinter import *
from tkinter import ttk
import tkinter


from tkinter.font import BOLD
from tkinter.messagebox import showinfo
from tkinter.tix import LabelEntry
from turtle import back


coffee = Tk()
coffee.configure(background='#FFFAF0')
coffee.geometry("750x500+0+0")
coffee.title("Coffee Ordering App")

# Top Frame For Title
Tops = Frame (coffee, width = 750 , height = 200, bd = 12, relief = "raise", bg="#fff")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('Times New Roman', 25 , 'bold'), text="\tCoffee Ordering App\t")
lblTitle.grid(row=0, column=0)



# Bottom Frames containing 3 extra frames

BottomMainFrame = Frame (coffee, width = 750 , height = 500, bd=12, background="beige", relief="sunken")
BottomMainFrame.pack(side=BOTTOM)
 


#First Frame or f1 Frame
f1 = Frame (BottomMainFrame, width = 250 , height = 500, relief="raise", bd=12 )
f1.pack(side=LEFT)




# F1TOP Frame

f1TOP = Frame (f1, width = 250 , height = 250)
f1TOP.pack(side=TOP)

def openNewWindow():
    newWindow = Toplevel(coffee)
    newWindow.title("Welcome!")
    newWindow.geometry("300x300")
    


    Label(newWindow,
          text ="       Thank You for Signing in!", font=('Times New Roman', 16, 'bold')).grid()
         

    
Label(f1TOP, text="Customer", font=('Times New Roman', 14, 'bold', )).grid(row=1, column=1)

name = Label(f1TOP, text="Name")
PhoneNumber = Label(f1TOP, text="Phone Number")
Address = Label(f1TOP, text="Address")

name.grid(row=2, column=0)
PhoneNumber.grid(row=3, column=0)
Address.grid(row=4, column=0)

namevalue = StringVar
phonevalue = StringVar
addressvalue = StringVar
checkvalue = IntVar

nameentry= Entry(f1TOP, textvariable=namevalue)
PhoneNumberentry= Entry(f1TOP, textvariable=phonevalue)
Addressentry= Entry(f1TOP, textvariable=addressvalue)

nameentry.grid(row=2, column=1)
PhoneNumberentry.grid(row=3, column=1)
Addressentry.grid(row=4, column=1)

btn = Button(f1TOP,
             text ="Submit!",
             command = openNewWindow)
btn.grid(row=5, column=1)
# F1BOTTOM Frame

f1BOTTOM = Frame (f1, width = 240 , height =  190, relief="sunken", bd = 12)
f1BOTTOM.pack(side=BOTTOM)

window = Canvas(f1BOTTOM, width= 250, height =200,)
window.pack()
image = PhotoImage(file='C:\\Users\\grimp\\Downloads\\coffee.png')
window.create_image(0,0, anchor = NW, image= image)

# f2 Frame
f2 = Frame (BottomMainFrame, width = 212 , height = 425, bd=12, relief="raise")
f2.pack(side=LEFT)

Label(f2, text="Coffee Choices:", font=('Times New Roman', 14, 'bold', )).pack()

def select(option):
    print(option)

ttk.Button(f2, text='Americano', command=lambda: select('Americano')).pack()
ttk.Button(f2, text='Arabica',command=lambda: select('Arabica')).pack()
ttk.Button(f2, text='Espresso', command=lambda: select('Espresso')).pack()
ttk.Button(f2, text='Cappucino', command=lambda: select('Capuccino')).pack()
ttk.Button(f2, text='Macchiato',command=lambda: select('Macchiato')).pack()
ttk.Button(f2, text='Verano', command=lambda: select('Verano')).pack()
ttk.Button(f2, text='Liberica',command=lambda: select('Liberica')).pack()
ttk.Button(f2, text='Robusta', command=lambda: select('Robusta')).pack()

label = Label(f2)
label.pack()

# f3 Frame

f3 = Frame (BottomMainFrame, width = 350 , height = 425, bd=12, relief="raise",)
f3.pack(side=RIGHT)

Label(f3, text="Special Req.(Ex. Whipped, Nutmeg, etc.)", font=('Times New Roman', 9,'bold' )).pack()




def myClick():
    newWindow = Toplevel(coffee)
    newWindow.title("Welcome!")
    newWindow.geometry("500x300")
    

    Label(newWindow,
          text ="Thank you, Your Order will be Ready in 10 mins.", font=('Times New Roman', 16, 'bold')).grid()


e = Entry(f3, width = 100)
e.pack()

myButton = Button(f3, text="Submit", command=myClick)
myButton.pack()

exit_button = Button(f3, text="Exit", command=coffee.destroy)
exit_button.pack(pady=10)
coffee.mainloop()
