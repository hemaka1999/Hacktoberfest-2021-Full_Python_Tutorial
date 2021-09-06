from tkinter import *

root=Tk()
root.title("How to use uniodes and special characters with tkinter")

my_label=Label(root,text='Dila'+u'\u00b0',font=("Helvetica",32)).pack(pady=4)
my_label=Label(root,text='Dila'+u'\u0DA9\u0DD2',font=("Helvetica",32)).pack(pady=4)

my_label=Label(root,text='Dila'+u'\u0DB8\u0DCA',font=("Helvetica",32)).pack(pady=4)
my_label=Label(root,text='Dila'+u'\u0DB3\u0DD4',font=("Helvetica",32)).pack(pady=4)
my_label=Label(root,text='Dila'+u'\u0D91',font=("Helvetica",32)).pack(pady=4)
my_label=Label(root,text='Dila'+u'\u0020\u0DBB\u0DD0',font=("Helvetica",32)).pack(pady=4)

root.mainloop()