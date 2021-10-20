from tkinter import *

root = Tk()
root.title("Data Entry")
root.geometry("500x500")

#entry box
Label(text="name").grid(row=0)
Label(text="lastname").grid(row=1)
Label(text="phone").grid(row=2)

et1 = Entry()
et1.grid(row=0, column=1)
et1.insert(0, "KOPE")

et2 = Entry()
et2.grid(row=1, column=1)
et2.insert(0, "SOLO")

et3 = Entry()
et3.grid(row=2, column=1)
et3.insert(0, "0812345678")

def deletText():
    et1.delete(0, END)
    et2.delete(0, END)
    et3.delete(0, END)

button = Button(text="Clear data", command=deletText).grid(row=3, column=1)

root.mainloop()