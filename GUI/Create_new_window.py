from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("CNW")
def open():
    global image
    top = Toplevel()
    top.title('Image')
    image = ImageTk.PhotoImage(Image.open('compass.png'))
    label=Label(top, image=image)
    label.pack()
    btn2 = Button(top, text="close", command=top.destroy)
    btn2.pack()
btn=Button(root,text="open",command=open)
btn.pack()





mainloop()