from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("radio button")
root.iconbitmap('F:\Programming Languages\Python\GUI\compass.png')
fan=StringVar()
fan.set("slow")
modes=[
    ("fast","1"),
    ("medium","2"),
    ("slow","3")
]

r=IntVar()
r.set("2")
for mode,value in modes:
    Radiobutton(root,text=value,variable=fan,value=mode).pack()
def clicked(value):
    label = Label(root, text=value)
    label.pack()


Radiobutton(root, text="Option 1", variable=r,value="1").pack()
Radiobutton(root, text="Option 2", variable=r,value="2").pack()
Radiobutton(root, text="Option 3", variable=r,value="3").pack()
button=Button(root,text="clicked_here", command=lambda:clicked(r.get()))
button.pack()


root.mainloop()