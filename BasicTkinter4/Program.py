from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")


myMenu = Menu()
root.config(menu=myMenu)

#Create new window
def showWindow():
    window = Tk()
    window.title("New window")
    window.geometry("200x200")
    window.mainloop

menuItem = Menu()
menuItem.add_command(label="New Window", command=showWindow)
menuItem.add_command(label="Open")
menuItem.add_command(label="Save")
menuItem.add_command(label="About")
menuItem.add_command(label="Exit")

myMenu.add_cascade(label="File", menu=menuItem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")

root.mainloop()