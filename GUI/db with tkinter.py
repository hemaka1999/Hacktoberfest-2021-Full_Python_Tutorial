from tkinter import *
import sqlite3
root=Tk()
con=sqlite3.connect('pyexample.db')
c=con.cursor()
oid=0
#Add the data
def submit():
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS student_info(
        S_ID int PRIMARY_KEY,
        First_name text,
        Second_name text,
        Age int,
        Email text,
        Phone_no text
        )
        """
    )
    con.commit()

    c.execute(
        "INSERT INTO student_info VALUES(:fname,:sname,:age,:email,:phone_no)",
        {
            'fname':f_name.get(),
            'sname':s_name.get(),
            'age':age.get(),
            'email':email.get(),
            'phone_no':phone_no.get()
        }
    )
    con.commit()

def update():
    c.execute(
        f"""
            UPDATE student_info SET     
            'fname':f_name.get(),
            'sname':s_name.get(),
            'age':age.get(),
            'email':email.get(),
            'phone_no':phone_no.get() 
             WHERE oid={id}
         """
    )
    con.commit()

    # clear text
    f_name.delete(0, END)
    s_name.delete(0, END)
    age.delete(0, END)
    email.delete(0, END)
    phone_no.delete(0, END)


#Display the data
def show():
   x=c.execute(
        """
        SELECT *,oid FROM student_info
        """
    )

   def edit(oid):
       editor = Tk()
       print(oid)
       f_name_label = Label(editor,text="First Name")
       f_name_label.grid(row=0, column=0)
       f_name = Entry(editor, width=30)
       f_name.grid(row=0, column=1, padx=20, pady=10)
       s_name_label = Label(editor,text="Second Name")
       s_name_label.grid(row=1, column=0)
       s_name = Entry(editor, width=30)
       s_name.grid(row=1, column=1, padx=20, pady=10)
       age_label = Label(editor,text="Age")
       age_label.grid(row=2, column=0)
       age = Entry(editor, width=30)
       age.grid(row=2, column=1, padx=20, pady=10)
       email_label = Label(editor,text="Email")
       email_label.grid(row=3, column=0)
       email = Entry(editor, width=30)
       email.grid(row=3, column=1, padx=20, pady=10)
       phone_label = Label(editor,text="Phone number")
       phone_label.grid(row=4, column=0)
       phone_no = Entry(editor, width=30)
       phone_no.grid(row=4, column=1, padx=20, pady=10)
       submit_btn = Button(editor, text="Update", command=update)
       submit_btn.grid(row=5, column=1, columnspan=2, pady=10, padx=10, ipadx=100)
       editor.mainloop()


   # delete records
   def delete(id):
       print(id)
       c.execute(
           f"""
           DELETE FROM student_info WHERE oid={id}
           """
       )


   fname = Label(text="First_name")
   sname = Label(text="Second name")
   age = Label(text="Age")
   email = Label(text="email")
   pn = Label(text="Phone number")
   fname.grid(row=8, column=0)
   sname.grid(row=8, column=1)
   age.grid(row=8, column=2)
   email.grid(row=8, column=3)
   pn.grid(row=8, column=4)
   i = 9

   for l in x.fetchall():
       global oid
       print(l)
       print(len(x.fetchall()))
       fname_l = Label(text=l[0])
       sname_l = Label(text=l[1])
       age_l = Label(text=l[2])
       email_l = Label(text=l[3])
       pn_l = Label(text=l[4])
       fname_l.grid(row=i, column=0)
       sname_l.grid(row=i, column=1)
       age_l.grid(row=i, column=2)
       email_l.grid(row=i, column=3)
       pn_l.grid(row=i, column=4)

       edit_btn=Button(root,text="Edit", command=lambda oid=i-8: edit(oid))
       edit_btn.grid(row=i, column=5, pady=10, padx=10)

       delete_btn = Button(root, text="Delete", command=lambda oid=i-8: delete(oid))
       delete_btn.grid(row=i, column=6, pady=10, padx=10)

       i = i + 1

   con.commit()

#edit records


f_name_label=Label(text="First Name")
f_name_label.grid(row=0,column=0)
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=10)
s_name_label=Label(text="Second Name")
s_name_label.grid(row=1,column=0)
s_name=Entry(root,width=30)
s_name.grid(row=1,column=1,padx=20,pady=10)
age_label=Label(text="Age")
age_label.grid(row=2,column=0)
age=Entry(root,width=30)
age.grid(row=2,column=1,padx=20,pady=10)
email_label=Label(text="Email")
email_label.grid(row=3,column=0)
email=Entry(root,width=30)
email.grid(row=3,column=1,padx=20,pady=10)
phone_label=Label(text="Phone number")
phone_label.grid(row=4,column=0)
phone_no=Entry(root,width=30)
phone_no.grid(row=4,column=1,padx=20,pady=10)
submit_btn=Button(root,text="Submit",command=submit)
submit_btn.grid(row=5,column=1,columnspan=2,pady=10,padx=10,ipadx=100)
show_btn=Button(root,text="show",command=show)
show_btn.grid(row=6,column=1,columnspan=2,pady=10,padx=10,ipadx=100)



mainloop()