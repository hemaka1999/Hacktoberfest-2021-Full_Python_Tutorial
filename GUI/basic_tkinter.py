from tkinter import *
root=Tk()

label1=Label(root,text='lal',fg='#456fff')
label1.pack()
e2=Entry(root,text='add something')
e2.pack()

def click():
    label2=Label(root,text=e2.get(),bg='#56ddad')
    label2.pack()

btn1=Button(root,text='click_me',command=click)
btn1.pack()
mainloop()