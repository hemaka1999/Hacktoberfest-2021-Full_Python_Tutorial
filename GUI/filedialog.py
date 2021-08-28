from tkinter import *
from tkinter import filedialog

root=Tk()
def select():
    filelocation = filedialog.askopenfilename(initialdir='c:/', title='select path', filetypes=(
    ('png files', "*.png"), ('jpg files', "*.jpg"), ('all files', "*")))
    path = Label(text=filelocation)
    path.pack()

btn=Button(root,text="open",command=select)
btn.pack()

mainloop()