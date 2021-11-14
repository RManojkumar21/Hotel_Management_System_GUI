from tkinter import *
from Food import *
from ViewFood import *
from PIL import ImageTk,Image #PIL -> Pillow


c=0
def destroy():
    global c
    c=0
    root.destroy()

def exit():
    "dummy function"
    pass

def foodsection():
    global c,root
    c+=1
    if c==1:
        root=Toplevel()
        root.title("Food Section")
        root.geometry("950x713")
        root.resizable(False,False)
        root.protocol("WM_DELETE_WINDOW",exit)
        bg=ImageTk.PhotoImage(file="Food.png")
        label=Label(root,image=bg)
        label.pack()
        Button(root,text="ADD FOOD STOCKS",font=("mono",13,"bold"),command=food).place(x=780,y=60)
        Button(root,text="VIEW FOOD STOCKS",font=("mono",13,"bold"),command=viewfood).place(x=780,y=100)
        Button(root, text='back', borderwidth=0,height=1,width=5,command=destroy).place(x=40,y=640)
        root.mainloop()

