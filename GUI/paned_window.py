from tkinter import *

root=Tk()
root.title('pane window')
root.geometry("400x400")

#panels
panel_1=PanedWindow(bd=4,relief="raised",bg="red")
panel_1.pack(fill=BOTH,expand=1)
left_label=Label(panel_1,text="Left Panel1")
panel_1.add(left_label)

#2nd panel
panel_2=PanedWindow(panel_1,orient=VERTICAL,bd=4,relief="raised",bg="green")
panel_1.add(panel_2)

top=Label(panel_2,text="Top panel 1")
panel_2.add(top)

bottum=Label(panel_2,text="Bottom panel")
panel_2.add(bottum)

panel_3=PanedWindow(panel_2,orient=HORIZONTAL,bd=4,relief='raised',bg='blue')
panel_2.add(panel_3)
left=Label(panel_3,text="Left Panel")
panel_3.add(left)
right=Label(panel_3,text="Right Panel")
panel_3.add(right)



root.mainloop()