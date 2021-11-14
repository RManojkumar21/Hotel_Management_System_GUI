from tkinter import*
from tkinter import messagebox
import pymysql

con=pymysql.connect(host="localhost",user="root",password='',database='Hotel Management')
cur=con.cursor()

c=0
def destroy():
    global c
    c=0
    root8.destroy()
    
def exit():
    "dummy function"
    pass

def viewEmployee():
    global c,root8
    c+=1
    if c==1:   
        root8=Toplevel()
        root8.title("Employee Section")
        root8.resizable(False,False)
        root8.geometry("1400x750")
        root8.protocol("WM_DELETE_WINDOW",exit)
        root8.configure(bg="gray21")
        Label(root8,text="",bg="gray21").pack()
        Label(root8,text="EMPLOYEE RECORD",bg="light Grey",fg="Black",font=("ubuntu",30,"italic"),width=16).pack()
        Label(root8,text="",bg="gray21",height=3).pack()
        #back
        Button(root8,text="QUIT",highlightbackground="light Grey",fg="black",width=10,height=2,command=destroy).place(x=660,y=680)
        #container
        Lf=Frame(root8,bg="ivory2",width=1300,height=530)
        Lf.pack()
        Label(Lf, text="%-22s%-10s%-12s%-10s%-25s%-33s%-30s%-12s%-16s%-18s%-20s%-25s%-12s%-5s"%('NAME', 'AGE', 'DOB', 'GENDER', 'CONTACT', 'EMAIL', 'ADDRESS', 'CITY', 'STATE', 'DEPARTMENT', 'STATUS', 'IDPROOF', 'TYPE', 'SALARY'),bg='ivory2',fg='black').place(x=10,y=20)
        Label(Lf, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='ivory2',fg='black').place(x=10,y=50)
        view="select NAME from Employee"
        view1="select AGE, DOB from Employee"
        view2="select GENDER from Employee"
        view3="select CONTACT from Employee"
        view4="select EMAIL from Employee"
        view5="select ADDRESS from Employee"
        view6="select CITY from Employee"
        view7="select STATE from Employee"
        view8="select DEPARTMENT from Employee"
        view9="select STATUS from Employee"
        view10="select IDPROOF from Employee"
        view11="select TYPE from Employee"
        view12="select SALARY from Employee"

        n=80
        results=cur.execute(view)
        con.commit()
        if results:

            for i in cur:
                Label(Lf,text="%-15s"%(i[0]),bg='ivory2',fg='black').place(x=9,y=n)
                n+=30
            a=80
            cur.execute(view1)
            con.commit()
            for i in cur:
                Label(Lf,text="%-5s%-5s"%(i[0],i[1]),bg='ivory2',fg='black').place(x=112,y=a)
                a+=30
            b=80
            cur.execute(view2)
            con.commit()
            for i in cur:
                Label(Lf,text="%-8s"%(i[0]),bg='ivory2',fg='black').place(x=227,y=b)
                b+=30
            c=80
            cur.execute(view3)
            con.commit()
            for i in cur:
                Label(Lf,text="%-8s"%(i[0]),bg='ivory2',fg='black').place(x=280,y=c)
                c+=30
            d=80
            cur.execute(view4)
            con.commit()
            for i in cur:
                Label(Lf,text="%-8s"%(i[0]),bg='ivory2',fg='black').place(x=367,y=d)
                d+=30
            e=80
            cur.execute(view5)
            con.commit()
            for i in cur:
                Label(Lf,text="%-8s"%(i[0]),bg='ivory2',fg='black').place(x=509,y=e)
                e+=30
            f=80
            cur.execute(view6)
            con.commit()
            for i in cur:
                Label(Lf,text="%-8s"%(i[0]),bg='ivory2',fg='black').place(x=685,y=f)
                f+=30
            g=80
            cur.execute(view7)
            con.commit()
            for i in cur:
                Label(Lf,text="%-8s"%(i[0]),bg='ivory2',fg='black').place(x=755,y=g)
                g+=30
            h=80
            cur.execute(view8)
            con.commit()
            for i in cur:
                Label(Lf,text="%-8s"%(i[0]),bg='ivory2',fg='black').place(x=838,y=h)
                h+=30
            j=80
            cur.execute(view9)
            con.commit()
            for i in cur:
                Label(Lf,text="%-8s"%(i[0]),bg='ivory2',fg='black').place(x=955,y=j)
                j+=30
            k=80
            cur.execute(view10)
            con.commit()
            for i in cur:
                Label(Lf,text="%-8s"%(i[0]),bg='ivory2',fg='black').place(x=1010,y=k)
                k+=30
            l=80
            cur.execute(view11)
            con.commit()
            for i in cur:
                Label(Lf,text="%-8s"%(i[0]),bg='ivory2',fg='black').place(x=1158,y=l)
                l+=30
                z=80
            cur.execute(view12)
            con.commit()
            for i in cur:
                Label(Lf,text="%-8s"%(i[0]),bg='ivory2',fg='black').place(x=1235,y=z)
                z+=30

        else:
            Label(Lf,text="No records",bg="ivory2",fg="black",font=("ubuntu",15,"italic")).place(x=615,y=260)

        root8.mainloop()

