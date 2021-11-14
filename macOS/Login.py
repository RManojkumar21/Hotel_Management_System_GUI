from tkinter import *
from Section import *
from tkinter import messagebox
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql

#connecting to the database
connectiondb = pymysql.connect(host="localhost",user="root",passwd="",database="Hotel Management")
cursordb = connectiondb.cursor()


c=0
def destroy():
    global c
    c=0
    root2.destroy()

def login_verification():
    user_verification = username.get()
    pass_verification = password.get()
    sql = "select * from adminlogin where Username = %s and Password = %s"
    cursordb.execute(sql,[(user_verification),(pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            section()
            break
    else:
        messagebox.showerror("Error","Invalid Username or Password")
        
#To disable the close button
def exit():
    "dummy function"
    pass


def Loginform():
    global root2
    global message
    global username
    global password
    global c,root2
    c+=1
    if c==1:
        root2=Toplevel()
        root2.title("Login Form")
        root2.geometry("900x650")
        root2.resizable(False,False)
        root2.protocol("WM_DELETE_WINDOW",exit)
        bg1=ImageTk.PhotoImage(file='pics.png')
        label1=Label(root2,image=bg1)
        label1.pack()
    
        username = StringVar()
        password = StringVar()
    
        #Creating layout of login form
        Label(root2,bd=18,relief=GROOVE,width=108,text="ADMIN LOGIN",font=("times new roman",15,"bold"), bg="Black",fg="White").place(x=0,y=0)
        #Username Label
        Label(root2,bd=10,bg="black",relief=GROOVE,fg="white",font=("times new roman",15,"bold"),text="Username * ").place(x=400,y=80)
        #Username textbox
        Entry(root2,bd=5,bg="white",width=30,textvariable=username).place(x=305,y=140)
        #Password Label
        Label(root2,bd=10,relief=RIDGE,fg="white",bg="black",font=("times new roman",15,"bold"),text="Password * ").place(x=400,y=200)
        #Password textbox
        Entry(root2,bd=5,bg="white",width=30,textvariable=password ,show="*").place(x=305,y=260)
        #Login button
        Button(root2,bd=5,text="LOGIN",font=("times new roman",12,"bold"),width=10, height=2,fg="black",relief=GROOVE,command=login_verification).place(x=420,y=320)        
        Button(root2,bd=5,text="EXIT",font=("times new roman",12,"bold"),width=10, height=1,fg="black",relief=GROOVE,command=destroy).place(x=800,y=600)
        root2.mainloop()

