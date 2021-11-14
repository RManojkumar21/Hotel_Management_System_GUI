from tkinter import *
from Employee import *
from ViewEmployee import *
from tkmacosx import CircleButton
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
        Button(root,text="ADD EMPLOYEE",font=("mono",13,"bold"),command=employee).place(x=40,y=60)
        Button(root,text="VIEW EMPLOYEE",font=("mono",13,"bold"),command=viewEmployee).place(x=40,y=100)
        Button(root, text='back', borderwidth=0,height=1,width=5,command=destroy).place(x=800,y=510)
        root.mainloop()

