from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("message box")
def popup():
    # messagebox.showinfo("This is my pop up","hello world")
    # messagebox.showwarning("Warn","Warn")
    messagebox.showerror("error","error")
def dialogbox():
    response=messagebox.askyesno("yes or no","hello")
    if response==1:
        Label(root,text="you clicked yes").pack()
    else:
        Label(root,text="you clicked No").pack()

Button(root,text="popup", command=popup).pack()
Button(root,text="yes or no", command=dialogbox).pack()

mainloop()