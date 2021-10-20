from tkinter import *

root = Tk()
root.title("My GUI")

#add text on display
# myLabel1 = Label(root, text="Hello World!", fg="red", font=20, bg="yellow").pack()
# myLabel2 = Label(root, text="KOPE").pack()

#place
# myLabel1 = Label(root, text="Hello World!", fg="red", font=20, bg="yellow").place(x=50, y=0)

#grid
# myLabel1 = Label(root, text="Hello World!", fg="red", font=20, bg="yellow").grid(row=0, column=0)
# myLabel2 = Label(root, text="KOPE", fg="red", font=20, bg="yellow").grid(row=1, column=0)

#Button
# btn1 = Button(root, text="Save", fg="white", bg="red").pack()
# btn2 = Button(root, text="Cancel", fg="white", bg="green").pack()

#Button fcommand
def showMessage():
    # print("Hello World!")
    # Label(root, text="Hello World!", fg="red", font=20, bg="yellow").pack()
#text box
    message = txt.get()
    print(message)
    Label(root, text=message, fg="red", font=20, bg="yellow").pack()
txt = StringVar()
myText = Entry(root, textvariable=txt).pack()
btn1 = Button(root, text="Save", fg="white", bg="red", command=showMessage).pack()
btn2 = Button(root, text="Cancel", fg="white", bg="green").pack()


#difine size and location : wxh+x+y
root.geometry("600x200+0+0")
root.mainloop()