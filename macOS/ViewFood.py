from tkinter import*
from tkinter import messagebox
import pymysql

con=pymysql.connect(host="localhost",user="root",password='',database='Hotel Management')
cur=con.cursor()

c=0
def destroy():
    global c
    c=0
    root9.destroy()

def exit():
    "dummy function"
    pass

def viewfood():
    global c,root9
    c+=1
    if c==1:
        root9=Toplevel()
        root9.title("Food Section")
        root9.resizable(False,False)
        root9.geometry("1000x750")
        root9.protocol("WM_DELETE_WINDOW",exit)
        root9.configure(bg="tomato")
        Label(root9,text="",bg="tomato").pack()
        Label(root9,text="FOOD STOCKS",bg="light Grey",fg="Black",font=("mono",30,"italic"),width=14).pack()
        Label(root9,text="",bg="tomato",height=3).pack()
        #quit
        Button(root9,text="QUIT",highlightbackground="light Grey",fg="black",width=10,height=2,command=destroy).place(x=455,y=680)
        #container
        Lf=Frame(root9,bg="ivory2",width=800,height=530)
        Lf.pack()
    
        Label(Lf, text="%-80s%-72s%-50s"%('STOCKNAME', 'QUANTITY', 'TOTALCOST'),bg='ivory2',fg='black').place(x=40,y=20)
        Label(Lf, text="-------------------------------------------------------------------------------------------------------------------------",bg='ivory2',fg='black').place(x=30,y=50)
        view="select STOCKNAME from Food"
        view1="select QUANTITY from Food"
        view2="select TOTALCOST from Food"
        n=70
        results=cur.execute(view)
        con.commit()
        if results:
        
            for i in cur:
                Label(Lf,text="%-80s"%(i[0]),bg='ivory2',fg='black').place(x=30,y=n)
                n+=30
            a=70
            cur.execute(view1)
            con.commit()
            for i in cur:
                Label(Lf,text="%-80s"%(i[0]),bg='ivory2',fg='black').place(x=380,y=a)
                a+=30
            b=70
            cur.execute(view2)
            con.commit()
            for i in cur:
                Label(Lf,text="%-80s"%(i[0]),bg='ivory2',fg='black').place(x=675,y=b)
                b+=30
        else:
            Label(Lf,text="No records",bg="ivory2",fg="black",font=("ubuntu",15,"italic")).place(x=370,y=260)

        root9.mainloop()

        

