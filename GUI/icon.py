from tkinter import *
from PIL import ImageTk,Image
root =Tk()
root.title("Example")
root.iconbitmap('F:\Programming Languages\Python\GUI\compass.png')
img=ImageTk.PhotoImage(Image.open("compass.png"))
label=Label(image=img)
label.pack()

mainloop()
