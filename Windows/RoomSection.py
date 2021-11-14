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
        Button(root,text="ADD CUSTOMER",font=("mono",11,"bold"),command=room).place(x=800,y=50)
        Button(root,text="VIEW CUSTOMER",font=("mono",11,"bold"),command=viewroom).place(x=800,y=90)
        Button(root,bd=5,bg="White",width=6,fg="Black",font=("mono",9,"bold"),text="Back",command=destroy).place(x=40,y=530)
        root.mainloop()


