from tkinter import *
root=Tk()
e=Entry(root,width="45",bg="#000", fg='#ffffff')
e.grid(row=5,column=0)
label=Label(root,text="hi")
label1=Label(root,text=5)

label.grid(row=0,column=0)
label1.grid(row=1,column=0)

def myclick():
    global label2
    label2=Label(root,text="ha")
    label2.grid(row=2, column=0)


button=Button(root,text="click me",command=myclick)
button.grid(row="4",column=1)



root.mainloop()