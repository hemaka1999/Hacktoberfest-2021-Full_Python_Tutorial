from tkinter import *
root =Tk()
root.title("drop Box")

clicked=StringVar()
clicked.set("Monday")
clicked2=StringVar()
options=["car","van","Lorry","Bus"]
def show():
    label=Label(text=clicked.get())
    label.pack()

def show2():
    label2=Label(text=clicked2.get())
    label2.pack()
drop=OptionMenu(root, clicked,"Monday","thusday","Wendsday","Thusrsday","Friday")
drop.pack()
btn=Button(root,text="show selection",command=show)
drop2=OptionMenu(root, clicked2,*options)
btn2=Button(root,text="show selection",command=show2)


drop.pack()
btn.pack()
drop2.pack()
btn2.pack()
mainloop()