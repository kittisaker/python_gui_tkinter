from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def showChoice():
    print(language1.get(), language2.get(), language3.get(), language4.get())

#Checkbutton : 0=choot 1=not choot
language1 = IntVar()
language2 = IntVar()
language3 = IntVar()
language4 = IntVar()
Checkbutton(text="Python", variable=language1).pack(anchor=W)
Checkbutton(text="Java", variable=language2).pack(anchor=W)
Checkbutton(text="PHP", variable=language3).pack(anchor=W)
Checkbutton(text="C#", variable=language4).pack(anchor=W)

Button(text="Show chooter", command=showChoice).pack(anchor=W)
root.mainloop()