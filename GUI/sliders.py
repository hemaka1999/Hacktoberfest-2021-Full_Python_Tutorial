from tkinter import *
root=Tk()
verticle=Scale(root,from_=0,to=200)
verticle.pack()
horizontol=Scale(root,from_=0,to=200,orient=HORIZONTAL)
horizontol.pack()
def slide():
    label = Label(root, text=horizontol.get())
    label.pack()
    root.geometry(str(horizontol.get())+"x400")


btn=Button(root,text="Click me",command=slide).pack()
mainloop()