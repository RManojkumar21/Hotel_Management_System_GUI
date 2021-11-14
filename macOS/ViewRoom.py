from tkinter import*
from tkinter import messagebox
import pymysql

con = pymysql.connect(user='root', password='', host='localhost', database='Hotel Management')
cur = con.cursor()

c=0
def destroy():
    global c
    c=0
    root10.destroy()

def exit():
    "dummy function"
    pass

def viewroom():
    global c,root10
    c+=1
    if c==1:
        root10=Toplevel()
        root10.title("Room Section")
        root10.resizable(False,False)
        root10.geometry("1000x750")
        root10.protocol("WM_DELETE_WINDOW",exit)
        root10.configure(bg="sandybrown")
        Label(root10,text="",bg="sandybrown").pack()
        Label(root10,text="CUSTOMER & ROOM DETAILS",bg="light Grey",fg="Black",font=("ubuntu",30,"italic"),width=25).pack()
        Label(root10,text="",bg="sandybrown",height=3).pack()
        #quit
        Button(root10,text="QUIT",highlightbackground="light Grey",fg="black",width=10,height=2,command=destroy).place(x=450,y=680)
        #container
        Lf=Frame(root10,bg="light goldenrod",width=850,height=530)
        Lf.pack()
        n=70
        Label(Lf, text="%-20s%-20s%-20s%-20s%-22s%-20s%-15s"%('NAME', 'PHONENO', 'ROOMNO', 'MEALS', 'ROOMTYPE', 'CHECKIN', 'CHECKOUT'),bg='light goldenrod',fg='black').place(x=65,y=20)
        Label(Lf, text="--------------------------------------------------------------------------------------------------------------------------------",bg='light goldenrod',fg='black').place(x=30,y=50)
        view="select NAME from Room"
        view1="select PHONENO, ROOMNO, MEALS from Room"
        view2="select ROOMTYPE from Room"
        view3="select CHECKIN, CHECKOUT from Room"
        results=cur.execute(view)
        con.commit()
        if results:

            for i in cur:
                Label(Lf,text="%-20s"%(i[0]),bg='light goldenrod',fg='black').place(x=40,y=n)
                n+=30
            a=70
            cur.execute(view1)
            con.commit()
            for i in cur:
                Label(Lf,text="%-20s%-25s%-25s"%(i[0],i[1],i[2]),bg='light goldenrod',fg='black').place(x=160,y=a)
                a+=30
            b=70
            cur.execute(view2)
            con.commit()
            for i in cur:
                Label(Lf,text="%-20s"%(i[0]),bg='light goldenrod',fg='black').place(x=480,y=b)
                b+=30
            c=70
            cur.execute(view3)
            con.commit()
            for i in cur:
                Label(Lf,text="%-23s%-20s"%(i[0],i[1]),bg='light goldenrod',fg='black').place(x=605,y=c)
                c+=30

        else:
            Label(Lf,text="No records",bg="light goldenrod",fg="black",font=("ubuntu",15,"italic")).place(x=380,y=260)

        root10.mainloop()

