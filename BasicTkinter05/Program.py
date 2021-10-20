from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("My GUI")
root.geometry("500x500")


myMenu = Menu()
root.config(menu=myMenu)

def showWindow():
    window = Tk()
    window.title("New window")
    window.geometry("200x200")
    window.mainloop

#messagebox test
def aboutProgram():
    # print("Deverloper : KOPE")
    tkinter.messagebox.showinfo("Descripe of program", "Kope is deverloper")

def exitProgram():
    # pass
    confirm = tkinter.messagebox.askquestion("Confirm", "Do you want to close the program?")
    if confirm == "yes":
        root.destroy()

menuItem = Menu()
menuItem.add_command(label="New Window", command=showWindow)
menuItem.add_command(label="Open")
menuItem.add_command(label="Save")
menuItem.add_command(label="About", command=aboutProgram)
menuItem.add_command(label="Exit", command=exitProgram)

myMenu.add_cascade(label="File", menu=menuItem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")

root.mainloop()