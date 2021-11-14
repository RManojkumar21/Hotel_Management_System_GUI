from tkinter import *
from Room import *
from ViewRoom import *
from PIL import ImageTk,Image #PIL -> Pillow


c=0
def destroy():
    global c
    c=0
    root.destroy()

def exit():
    "dummy function"
    pass

def roomsection():
    global c,root
    c+=1
    if c==1:
        root=Toplevel()
        root.title("Room Section")
        root.geometry("968x600")
        root.resizable(False,False)
        root.protocol("WM_DELETE_WINDOW",exit)
        bg=ImageTk.PhotoImage(file="Room.png")
        label=Label(root,image=bg)
        label.pack()
        Button(root,text="ADD CUSTOMER",font=("mono",13,"bold"),command=room).place(x=800,y=50)
        Button(root,text="VIEW CUSTOMER",font=("mono",13,"bold"),command=viewroom).place(x=800,y=90)
        Button(root, text='back', borderwidth=0,height=1,width=5,command=destroy).place(x=40,y=520)
        root.mainloop()

