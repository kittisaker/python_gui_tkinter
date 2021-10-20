from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

#check more choose
def showChoice():
    choice1 = language1.get()
    choice2 = language2.get()
    choice3 = language3.get()
    choice4 = language4.get()
    if choice1 == 1:
        Label(text="Choosed Python").pack(anchor=W)
    if choice2 == 1:
        Label(text="Choosed Java").pack(anchor=W)
    if choice3 == 1:
        Label(text="Choosed PHP").pack(anchor=W)
    if choice4 == 1:
        Label(text="Choosed C#").pack(anchor=W)

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