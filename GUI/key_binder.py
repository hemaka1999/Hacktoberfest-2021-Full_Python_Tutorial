from tkinter import *
root=Tk()


def clicker(event):
    label=Label(root,text=f"LAL coordinates x- {event.x},y-{event.y}")
    label.pack()

def clicker2(event):
    label=Label(root,text=f"LAL coordinates x- {event.x},y-{event.y}")
    label.pack()

def clicker3(event):
    label=Label(root,text=f"LAL coordinates x- {event.x},y-{event.y}")
    label.pack()

def clicker4(event):
    label=Label(root,text=f"You press {event.keysym}")
    label.pack()
mybutton=Button(root,text="Right Click")
mybutton.bind("<Button-1>", clicker)
mybutton.pack()


mybutton2=Button(root,text="Enter the Click")
mybutton2.bind("<Enter>", clicker2) #Leave #FocusIn #FocusOut
mybutton2.pack()

mybutton3=Button(root,text="Press enter")
mybutton3.bind("<Return>", clicker3)
mybutton3.pack()

mybutton4=Button(root,text="press any key")
mybutton4.bind("<Key>", clicker4)
mybutton4.pack()

root.mainloop()