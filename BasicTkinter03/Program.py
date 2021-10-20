from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

#Create menu
myMenu = Menu()
root.config(menu=myMenu)

#add menu
# myMenu.add_cascade(label="Menu1")
# myMenu.add_cascade(label="Menu2")
# myMenu.add_cascade(label="Menu3")

#add submenu (menu item)
menuItem = Menu()
menuItem.add_command(label="New File")
menuItem.add_command(label="Open")
menuItem.add_command(label="Save")
menuItem.add_command(label="About")
menuItem.add_command(label="Exit")
myMenu.add_cascade(label="Menu1", menu=menuItem)
myMenu.add_cascade(label="Menu2")
myMenu.add_cascade(label="Menu3")

root.mainloop()