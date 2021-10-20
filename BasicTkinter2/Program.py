from tkinter import *

#Display1
root = Tk()
root.title("My GUI")
root.geometry("500x500")

# #Display2
# myWindow = Tk()
# myWindow.title("Working Report")
# myWindow.geometry("500x300")


#in root
def showMessage():
    message = txt.get()
    Label(root, text=message, fg="red", font=20, bg="yellow").pack()

def openWindow():
    #Display2
    myWindow = Tk()
    myWindow.title("Working Report")
    myWindow.geometry("500x300")

txt = StringVar()
myText = Entry(root, textvariable=txt).pack()
btn1 = Button(root, text="Save", fg="white", bg="red", command=showMessage).pack()
btn2 = Button(root, text="Open report", fg="white", bg="green", command=openWindow).pack()

#in window
# myLabel = Label(myWindow, text="message1", fg="red", font=20, bg="yellow").pack()

root.mainloop()