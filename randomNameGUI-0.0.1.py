#imports the necessary libraries
from tkinter import *
from tkinter import messagebox
import random

#sets up the variable and list
amount=int("-1")
names=[]

#defines all the functions
def add():
    global amount
    if e1.get() != "":
        names.append(e1.get().capitalize())
        e1.delete(0, END) 
        amount = amount + 1

def addednames():
    global amount
    if amount > -1:
        messagebox.showinfo("Random Name Picker", "Currently, your names are" + str(names) + "'!")
    else:
        messagebox.showerror("Random Name Picker", "You need to add names first!")
    
def select():
    global amount
    if amount > -1:
        in1=e1.get()
        namechoice = random.randint(0, amount)
        messagebox.showinfo("Random Name Picker", "Your random name is '" + names[namechoice] + "'!")
    else:
        messagebox.showerror("Random Name Picker", "You need to add names first!\nUsing a predefined list of names will be added soon.")

def about():
    messagebox.showinfo("Random Name Picker", "Random Name Picker\nver 0.0.1 GUI Edition\nThis software was made by Tom Rolfe\nVisit my GitHub @ www.github.com/zeddytbr for more info!\nBased on Python - GUI made using TKinter\n\nLicensed under GNU General Public License V3.0")

#main window
master = Tk()
master.title("Random Name Picker")

menubar = Menu(master)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
master.config(menu=menubar)

Label(master, text="Random Name Picker\n\nInput a name then press add\nPress Choose when finished\n").pack()

Label(master, text="Name Input").pack()
e1 = Entry(master)
e1.pack(pady=10)


Button(master, text='Choose', command=select).pack(side=LEFT, padx=4, pady=4)
Button(master, text='Add Name', command=add).pack(side=LEFT, padx=4, pady=4)
Button(master, text='Added Names', command=addednames).pack(side=LEFT, padx=4, pady=4)

master.mainloop()


