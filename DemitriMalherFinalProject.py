from tkinter import *



coffee = Tk()
coffee.configure(background='#FFFAF0')
coffee.geometry("750x500+0+0")
coffee.title("Coffee Ordering App")


#Top Frame For Title
Tops = Frame (coffee, width = 750 , height = 100, bd= 12, relief="raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('Times New Roman', 25 , 'bold'), text="\tCoffee Ordering App\t")
lblTitle.grid(row=0, column=0)

#image




CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
C1 = Checkbutton(coffee, text = "Americano", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(coffee, text = "Red Eye", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C3 = Checkbutton(coffee, text = "Mocchiato", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C4 = Checkbutton(coffee, text = "Espresso", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()
C3.pack()
C4.pack()


coffee.mainloop()