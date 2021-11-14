from tkinter import *
from EmployeeSection import*
from FoodSection import*
from RoomSection import*
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql


con = pymysql.connect(user='root', password='', host='localhost', database='Hotel Management')

c=0
#password_updation
def change():
    new_password=newpass.get()
    re_password=repass.get()
    old_password=oldpass.get()
    
    if new_password!=re_password:
        messagebox.showerror("Error","Password not matched !")
    else:
        cur = con.cursor()
        password=("UPDATE adminlogin SET Password='"+new_password+"' where Password='"+old_password+"'")
        result=cur.execute(password)
        if result:
            con.commit()
            messagebox.showerror("Error","Password Changed !")
        else:
            con.rollback
            messagebox.showerror("Error","Invalid Old Password !")
            

def password():
    global newpass,repass,oldpass,c
    c+=1
    def exit():
        "dummy function"
        pass
    if c==1:
        root= Toplevel(root3)
        root.geometry("800x500")
        root.resizable(False,False)
        root.protocol("WM_DELETE_WINDOW",exit)
        root.title("Change Password")
        root.configure(bg="grey20")
        Label(root,text="",bg="grey20").pack()
        Label(root,text="New Password", bg='grey20',fg="white", font=('times new roman',20,"italic")).pack()
        Label(root,text="",bg="grey20").pack()
        newpass=Entry(root,bd=0,bg="white",width=25 ,show="*")
        newpass.pack()
        Label(root,text="",bg="grey20").pack()
        Label(root,text="Re-Enter Password", bg='grey20', fg="white",font=('times new roman',20,"italic")).pack()
        Label(root,text="",bg="grey20").pack()
        repass=Entry(root,bd=0,bg="white",width=25)
        repass.pack()
        Label(root,text="",bg="grey20").pack()
        Label(root,text="Old Password", bg='grey20', fg="white",font=('times new roman',20,"italic")).pack()
        Label(root,text="",bg="grey20").pack()  
        oldpass=Entry(root,bd=0,bg="white",width=25)
        oldpass.pack()
        Label(root,text="",bg="grey20",height=2).pack()  
        Button(root,bd=10,bg="White",height=2,width=16,fg="Black",font=("mono",11,"bold"),text="CHANGE PASSWORD",command=change).pack()
        Label(root,text="",bg="grey20",height=3).pack()
        Label(root,text="",bg="grey20",width=2).pack(side=RIGHT)
        def back():
            global c
            a=messagebox.askyesno("back","Do you want to go back")
            if a==1:
                c=0
                root.destroy()
            else:
                return
        
        Button(root,bd=10,bg="White",height=2,width=6,fg="Black",font=("mono",11,"bold"),text="back",command=back).pack(anchor=SE)
        root.mainloop()



#section_page
def logout():
    a=messagebox.askyesno("Log out","Do you want to log out?")
    if a==1:
        root3.destroy()
    else:
        return


def exit():
    "dummy function"
    pass


def section():
    global root3
    root3 = Toplevel()
    root3.geometry("1000x650")
    root3.resizable(False,False)
    root3.protocol("WM_DELETE_WINDOW",exit)
    root3.title('Choose Section')
    bg=ImageTk.PhotoImage(file="EL.png")
    label=Label(root3,image=bg)
    label.pack()
    Button(root3,bd=10,bg="White",fg="Black",font=("times new roman",16,"bold"),text="EMPLOYEE SECTION",command=empsection).place(x=50,y=400)
    Button(root3,bd=10,bg="White",fg="Black",font=("times new roman",16,"bold"),text="FOOD SECTION",command=foodsection).place(x=420,y=300)
    Button(root3,bd=10,bg="White",fg="Black",font=("times new roman",16,"bold"),text="ROOM SECTION",command=roomsection).place(x=750,y=200)
    Button(root3,bd=10,bg="White",fg="Black",font=("ubuntu",10,"bold"),text="CHANGE PASSWORD",command=password).place(x=1000,y=500,anchor="ne")
    Button(root3,bd=10,bg="White",fg="Black",font=("ubuntu",10,"bold"),text="LOG OUT",command=logout).place(x=1000,y=530,anchor="ne")
    root3.mainloop()

