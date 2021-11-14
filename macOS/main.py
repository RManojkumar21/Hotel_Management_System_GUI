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
Label(root,text='WELCOME  TO  HOTEL  ELITE ',bd=15,width="300",font=("times new roman",20,"bold"),relief=RIDGE,fg="White",bg="Black").pack()
button1=Button(root,text="ADMIN LOGIN",relief=GROOVE,font=("times new roman", 20,"bold"),fg="Black",highlightbackground="Black",width=15,height=2,bd=5,command=Loginform).place(x=60,y=170)
button2=Button(root,text="CLOSE APPLICATION",font=("times new roman",20,"bold"),fg="Black",highlightbackground="Black",width=25,height=2,bd=5,relief=GROOVE,command=root.destroy).place(x=60,y=230)
root.mainloop()




  
