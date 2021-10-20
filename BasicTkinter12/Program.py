from tkinter import *

root = Tk()
root.title("Data Entry")
root.geometry("500x500")

#Circle area = pi*(r*r)
Label(text="radius", font=30).grid(row=0, sticky=W)
radius = IntVar()
et1 = Entry(textvariable=radius, width=30, font=30)
et1.grid(row=0, column=1)

def calculate():
    et2.delete(0, END)
    area = 3.14 * (radius.get() * radius.get())
    et2.insert(0, area)
btn1 = Button(text="Calculate", command=calculate).grid(row=1, column=1, sticky=W)

def clearValue():
    et1.delete(0, END)
    et2.delete(0, END)
btn2 = Button(text="Clear value", command=clearValue).grid(row=1, column=1, sticky=E)

Label(text="circle area", font=30).grid(row=2, sticky=W)
et2 = Entry(width=30, font=30)
et2.grid(row=2, column=1)

root.mainloop()