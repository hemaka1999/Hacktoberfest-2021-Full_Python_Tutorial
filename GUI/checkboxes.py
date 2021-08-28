from tkinter import *

root=Tk()
var=StringVar()
c=Checkbutton(root,text="check this box, I dare you!",variable=var,onvalue="On",offvalue="Off")
c1=Checkbutton(root,text="check this box, I dare you!",variable=var,onvalue="O",offvalue="Off")
c.deselect()
c.pack()
c1.pack()
print(c)

def check():
    labe = Label(root, text=var.get()).pack()

mybutton=Button(root,text="Click me",command=check).pack()

mainloop()
