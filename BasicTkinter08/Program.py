from tkinter import *
from tkinter.filedialog import test
import tkinter.messagebox

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def shoChoice():
    choice = language.get()
    # print(choice)
    if choice == 1:
        tkinter.messagebox.showinfo("Alarm", "You are chooting Python langauge")
    elif choice == 2:
        tkinter.messagebox.showinfo("Alarm", "You are chooting Java langauge")
    elif choice == 3:
        tkinter.messagebox.showinfo("Alarm", "You are chooting PHP langauge")
    else :
        tkinter.messagebox.showinfo("Alarm", "You are chooting C# langauge")

#add chooter in program
language = IntVar()
#sit default
language.set(2)
Radiobutton(text="Python", variable=language, value=1, command=shoChoice).grid(row=0, column=0)
Radiobutton(text="Java", variable=language, value=2, command=shoChoice).grid(row=0, column=1)
Radiobutton(text="PHP", variable=language, value=3, command=shoChoice).grid(row=0, column=2)
Radiobutton(text="C#", variable=language, value=4, command=shoChoice).grid(row=0, column=3)

root.mainloop()