from tkinter import *
from tkinter import ttk

root = Tk()
root.title("combo box")
root.geometry("500x500")

#combobox
Label(text="Address", font=20).grid(row=0, column=0)
choice = StringVar(value="Choose province")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("Bankok", "Changmai", "Krabi", "Puket", "Chonburi")
combo.grid(row=0, column=1)

def selectCity():
    label1 = Label(text="You choosed = "+choice.get(), font=20).grid(row=2, column=1)

btn = Button(text="Send data", command=selectCity)
btn.grid(row=1, column=1)


root.mainloop()