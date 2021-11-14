from tkinter import *
from Employee import *
from ViewEmployee import *
from PIL import ImageTk,Image #PIL -> Pillow


c=0
def destroy():
    global c
    c=0
    root.destroy()

def exit():
    "dummy function"
    pass

def empsection():
    global c,root
    c+=1
    if c==1:
        root=Toplevel()
        root.title("Employee Section")
        root.geometry("900x600")
        root.resizable(False,False)
        root.protocol("WM_DELETE_WINDOW",exit)
        bg=ImageTk.PhotoImage(file="Emp.png")
        label=Label(root,image=bg)
        label.pack()
        Button(root,text="ADD EMPLOYEE",font=("mono",11,"bold"),command=employee).place(x=40,y=60)
        Button(root,text="VIEW EMPLOYEE",font=("mono",11,"bold"),command=viewEmployee).place(x=40,y=100)
        Button(root,bd=5,bg="White",width=6,fg="Black",font=("mono",9,"bold"),text="Back",command=destroy).place(x=810,y=540)
        root.mainloop()


