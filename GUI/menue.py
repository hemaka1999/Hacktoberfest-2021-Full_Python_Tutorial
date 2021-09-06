from tkinter import *


root=Tk()
root.title("Top Menue")
my_menue=Menu(root)
root.config(menu=my_menue)

def command():
    label=Label(text='Menu tab select')
    label.pack()

#Create menue tabs
file_menu=Menu(my_menue)
my_menue.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="new", command=command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu=Menu(my_menue)
my_menue.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="cut", command=command)
edit_menu.add_separator()
edit_menu.add_command(label="copy")
root.mainloop()