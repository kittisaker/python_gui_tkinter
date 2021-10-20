from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

#colorchooser
def selectColer():
    color = askcolor()
    print(color[1])
    myLabel = Label(text="Hello Python", fg=color[1]).pack()

btn = Button(text="Select color", command=selectColer).pack()

root.mainloop()