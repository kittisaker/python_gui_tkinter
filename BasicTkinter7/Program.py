from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def selectColer():
    color = askcolor()
    print(color[1])
    myLabel = Label(text="Hello Python", fg=color[1]).pack()

#Read file txt
def selectFile():
    fileOpen = askopenfilename() #askopenfile()
    fileContent = open(fileOpen, encoding="utf8")
    myLabel = Label(text=fileContent.read()).pack()

btn1 = Button(text="Select color", command=selectColer).pack()
btn2 = Button(text="Select file open (.txt for test)", command=selectFile).pack()

root.mainloop()