from tkinter import *
from Login import*
from PIL import ImageTk,Image #PIL -> Pillow

def exit():
    "dummy function"
    pass

root=Tk()
root.title("Hotel Elite")
root.geometry("1200x700")
root.resizable(False,False)
root.protocol("WM_DELETE_WINDOW",exit)
bg=ImageTk.PhotoImage(file="res.png")
label=Label(root,image=bg)
label.pack()
Button(root,text="ADMIN LOGIN",font=("times new roman", 15,"bold"),fg="black",bg="grey51",width=13,bd=0,relief=GROOVE,command=Loginform).place(x=50,y=205)
Button(root,text="CLOSE APPLICATION",font=("times new roman",15,"bold"),fg="black",bg="grey51",width=20,bd=0,relief=GROOVE,command=root.destroy).place(x=50,y=250)
root.mainloop()




  
