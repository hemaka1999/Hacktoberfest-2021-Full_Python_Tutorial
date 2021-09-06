from tkinter import *
from tkinter import ttk

root=Tk()
root.title("dropdown menu")
clicked=StringVar()
options=["Mon","Tue","Wedn","Thu","Fri","Sat","Sun"]
clicked.set(options[0])
def selected(event):
    label=Label(text=clicked.get())
    label.pack()

def combo_click(event):
    label=Label(text="combo clicked")
    label.pack()
drop=OptionMenu(root,clicked,*options,command=selected)
drop.pack()
mycombo=ttk.Combobox(root,value=options)
mycombo.current(0)
mycombo.bind("<<ComboboxSelected>>",combo_click)
mycombo.pack()
root.mainloop()