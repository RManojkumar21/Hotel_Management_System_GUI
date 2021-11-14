from tkinter import*
from tkinter import messagebox
from app import calc
import pymysql

#connection to database
con = pymysql.connect(user='root', password='', host='localhost', database='Hotel Management')

c=0
def receipt():
    global root6
    try:
        a=t.get()
        b=t1.get()
        c=t2.get()
        total=int(a)+int(b)+int(c)
        qf=int(qf1.get())+int(qf2.get())+int(qf3.get())+int(qf4.get())+int(qf5.get())
        qs=int(qs1.get())+int(qs2.get())+int(qs3.get())+int(qs4.get())+int(qs5.get())
        qn=int(qn1.get())+int(qn2.get())+int(qn3.get())+int(qn4.get())+int(qn5.get())
        rootsub=Toplevel(root6)
        rootsub.geometry("370x250")
        rootsub.resizable(False,False)
        rootsub.title("Receipt")
        rootsub.configure(bg="ivory2")
        Label(rootsub,text="----------RECEIPT----------",bg="ivory2").place(relx=0.30,rely=0.04)
        Label(rootsub,text="Fruits & Vegetables",bg="ivory2").place(relx=0.13,rely=0.20)
        Label(rootsub,text="-",bg="ivory2").place(relx=0.51,rely=0.20)
        Label(rootsub,text=qf,bg="ivory2").place(relx=0.6,rely=0.20)
        Label(rootsub,text="-",bg="ivory2").place(relx=0.72,rely=0.20)
        Label(rootsub,text=a,bg="ivory2").place(relx=0.8,rely=0.20)
        Label(rootsub,text="Special Ingredients",bg="ivory2").place(relx=0.13,rely=0.36)
        Label(rootsub,text="-",bg="ivory2").place(relx=0.51,rely=0.36)
        Label(rootsub,text=qs,bg="ivory2").place(relx=0.6,rely=0.36)
        Label(rootsub,text="-",bg="ivory2").place(relx=0.72,rely=0.36)
        Label(rootsub,text=b,bg="ivory2").place(relx=0.8,rely=0.36)
        Label(rootsub,text="Non-Vegetables",bg="ivory2").place(relx=0.14,rely=0.52)
        Label(rootsub,text="-",bg="ivory2").place(relx=0.51,rely=0.52)
        Label(rootsub,text=qn,bg="ivory2").place(relx=0.6,rely=0.52)
        Label(rootsub,text="-",bg="ivory2").place(relx=0.72,rely=0.52)
        Label(rootsub,text=c,bg="ivory2").place(relx=0.8,rely=0.52)
        Label(rootsub,text="_____",bg="ivory2").place(relx=0.79,rely=0.59)
        Label(rootsub,text="₹",bg="ivory2").place(relx=0.76,rely=0.68)
        Label(rootsub,text=total,bg="ivory2").place(relx=0.8,rely=0.68)
        Label(rootsub,text="_____",bg="ivory2").place(relx=0.79,rely=0.75)
        def bill():
            #storing_stocks
            fruits=["Apples and Pears","Bananas and Mangoes ","Berries and Melons","Leafy green and Root","Cruciferous and Marrow",
                        "Maida and Wheet Flour","Special Masala","Rice","Dessert","Diary Products",
                        "Meat","Chicken","Beef","Eggs","Fish"]
            qty=[qf1.get(),qf2.get(),qf3.get(),qf4.get(),qf5.get(),qs1.get(),qs2.get(),qs3.get(),qs4.get(),qs5.get(),qn1.get(),qn2.get(),qn3.get(),qn4.get(),qn5.get()]
            cost=[f1.get(),f2.get(),f3.get(),f4.get(),f5.get(),sp1.get(),sp2.get(),sp3.get(),sp4.get(),sp5.get(),nv1.get(),nv2.get(),nv3.get(),nv4.get(),nv5.get()]
            cursor = con.cursor()
        
            stocks = (
                           "INSERT INTO Food(STOCKNAME, QUANTITY, TOTALCOST)"
                           "VALUES (%s, %s, %s)"
                   )
        
            a=messagebox.askyesno("Confirm","Confirm ?")
            if a==1:
                for i,j,k in zip(fruits,qty,cost):
        
                    data=(i, j, k)
                    print(data)
            
                    try:
                        #executing the sql command
                        cursor.execute(stocks,data)
                        #commit changes in database
                        con.commit()
                        rootsub.destroy()
                    except:
                        con.rollback()
                else:
                    return

        Button(rootsub,text="Bill",width=7,height=1,bd=1,command=bill).place(relx=0.4,rely=0.84)
        
    except:
        messagebox.showerror("Error","Field is Empty or Invalid Input !")
    

def total(n):
    global s,s1,s2
    s=""
    s1=""
    s2=""
    if n==1:
        try:
            a=f1.get()
            b=f2.get()
            c=f3.get()
            d=f4.get()
            e=f5.get()
            total=int(a)+int(b)+int(c)+int(d)+int(e)
            s=s+str(total)
            t.delete(0,END)
            t.insert(0,s)
        except:
            messagebox.showinfo("Warning","Field is Empty or Enter '0'")
    elif n==2:
        try:
            a1=sp1.get()
            b1=sp2.get()
            c1=sp3.get()
            d1=sp4.get()
            e1=sp5.get()
            total1=int(a1)+int(b1)+int(c1)+int(d1)+int(e1)
            s1=s1+str(total1)
            t1.delete(0,END)
            t1.insert(0,s1)
        except:
            messagebox.showinfo("Warning","Field is Empty or Enter '0'")

    elif n==3:
        try:
            a2=nv1.get()
            b2=nv2.get()
            c2=nv3.get()
            d2=nv4.get()
            e2=nv5.get()
            total2=int(a2)+int(b2)+int(c2)+int(d2)+int(e2)
            s2=s2+str(total2)
            t2.delete(0,END)
            t2.insert(0,s2)
        except:
            messagebox.showinfo("Warning","Field is Empty or Enter '0'")

def exit():
    "dummy function"
    pass
    
def food():
    global f1,f2,f3,f4,f5,sp1,sp2,sp3,sp4,sp5,nv1,nv2,nv3,nv4,nv5,eq,eq1,eq2
    global qf1,qf2,qf3,qf4,qf5,qs1,qs2,qs3,qs4,qs5,qn1,qn2,qn3,qn4,qn5
    global root6,t,t1,t2
    global c
    c+=1
    if c==1:
        root6=Toplevel()
        root6.title("Food Section")
        root6.resizable(False,False)
        root6.geometry("1200x720")
        root6.protocol("WM_DELETE_WINDOW",exit)
        root6.configure(bg="coral1")
        Label(root6,text="",bg="coral1").pack()
        Label(root6,text="FOOD STUFF",bg="light grey",fg="Black",font=("mono",21,"italic"),width=12).pack()
        #back
        def back():
            global c
            a=messagebox.askyesno("Warning!","Do you want to go back ?")
            if a==1:
                c=0
                root6.destroy()
            else:
                return
        
        Label(root6,text="",bg="coral1").pack(side=BOTTOM)
        Button(root6,bd=3,bg="White",width=6,fg="Black",font=("mono",8,"bold"),text="Back",command=back).place(x=1115,y=670)

        #container1
        Label(root6,text="",bg="coral1",width=2).pack(side=LEFT)
        Lf=Frame(root6,bg="springgreen3",width=360,height=500)
        Lf.pack(side=LEFT)
        Label(Lf,text="Fruits & Vegetables",fg="black",bg="springgreen3",font=("mono",14,"italic")).place(x=90,y=10)
        Label(Lf,text="-----------------------------------------------",bg="springgreen3").place(x=57,y=35)
        Label(Lf,text="Qty.",bg="springgreen3").place(x=210,y=60)
        Label(Lf,text="Price",bg="springgreen3").place(x=285,y=60)
        #fruits
        Label(Lf,text="Apples and Pears :",fg="black",bg="springgreen3",font=("mono",11,"italic")).place(x=20,y=90)
        qf1=Entry(Lf,bd=0,width=4)
        qf1.place(x=210,y=91)
        f1=Entry(Lf,bd=0,width=7)
        f1.place(x=280,y=91)
        Label(Lf,text="Bananas and Mangoes :",fg="black",bg="springgreen3",font=("mono",11,"italic")).place(x=20,y=150)
        qf2=Entry(Lf,bd=0,width=4)
        qf2.place(x=210,y=151)
        f2=Entry(Lf,bd=0,width=7)
        f2.place(x=280,y=151)
        Label(Lf,text="Berries and Melons :",fg="black",bg="springgreen3",font=("mono",11,"italic")).place(x=20,y=210)
        qf3=Entry(Lf,bd=0,width=4)
        qf3.place(x=210,y=211)
        f3=Entry(Lf,bd=0,width=7)
        f3.place(x=280,y=211)
        #vegetables
        Label(Lf,text="Leafy green and Root :",fg="black",bg="springgreen3",font=("mono",11,"italic")).place(x=20,y=270)
        qf4=Entry(Lf,bd=0,width=4)
        qf4.place(x=210,y=271)
        f4=Entry(Lf,bd=0,width=7)
        f4.place(x=280,y=271)
        Label(Lf,text="Cruciferous and Marrow :",fg="black",bg="springgreen3",font=("mono",11,"italic")).place(x=20,y=330)
        qf5=Entry(Lf,bd=0,width=4)
        qf5.place(x=210,y=331)
        f5=Entry(Lf,bd=0,width=7)
        f5.place(x=280,y=331)
        Label(Lf,text="Total :",fg="black",bg="springgreen3",font=("mono",11,"italic")).place(x=210,y=387)
        t=Entry(Lf,bd=0,width=7)
        t.place(x=280,y=390)
        #total
        Button(Lf,text="Total",highlightbackground="light Grey",width=10,height=2,command=lambda: total(1)).place(x=140,y=440)



        #container2
        Label(root6,text="",bg="coral1",width=3).pack(side=LEFT)
        Lf1=Frame(root6,bg="tan1",width=365,height=500)
        Lf1.pack(side=LEFT)
        Label(Lf1,text="Special Ingredients",fg="black",bg="tan1",font=("mono",14,"italic")).place(x=100,y=10)
        Label(Lf1,text="-------------------------------------------------",bg="tan1").place(x=57,y=35)
        Label(Lf1,text="Qty.",bg="tan1").place(x=210,y=60)
        Label(Lf1,text="Price",bg="tan1").place(x=285,y=60)
        #Ingredient
        Label(Lf1,text="Maida and Wheet Flour :",fg="black",bg="tan1",font=("mono",11,"italic")).place(x=20,y=90)
        qs1=Entry(Lf1,bd=0,width=4)
        qs1.place(x=210,y=91)
        sp1=Entry(Lf1,bd=0,width=7)
        sp1.place(x=280,y=91)
        Label(Lf1,text="Special Masala :",fg="black",bg="tan1",font=("mono",11,"italic")).place(x=20,y=150)
        qs2=Entry(Lf1,bd=0,width=4)
        qs2.place(x=210,y=151)
        sp2=Entry(Lf1,bd=0,width=7)
        sp2.place(x=280,y=151)
        Label(Lf1,text="Rice :",fg="black",bg="tan1",font=("mono",11,"italic")).place(x=20,y=210)
        qs3=Entry(Lf1,bd=0,width=4)
        qs3.place(x=210,y=211)
        sp3=Entry(Lf1,bd=0,width=7)
        sp3.place(x=280,y=211)
        #Dessert
        Label(Lf1,text="Dessert :",fg="black",bg="tan1",font=("mono",11,"italic")).place(x=20,y=270)
        qs4=Entry(Lf1,bd=0,width=4)
        qs4.place(x=210,y=271)
        sp4=Entry(Lf1,bd=0,width=7)
        sp4.place(x=280,y=271)
        Label(Lf1,text="Diary Products :",fg="black",bg="tan1",font=("mono",11,"italic")).place(x=20,y=330)
        qs5=Entry(Lf1,bd=0,width=4)
        qs5.place(x=210,y=331)
        sp5=Entry(Lf1,bd=0,width=7)
        sp5.place(x=280,y=331)
        Label(Lf1,text="Total :",fg="black",bg="tan1",font=("mono",11,"italic")).place(x=210,y=387)
        t1=Entry(Lf1,bd=0,width=7)
        t1.place(x=280,y=390)
        #total
        Button(Lf1,text="Total",highlightbackground="light Grey",width=10,height=2,command=lambda: total(2)).place(x=140,y=440)



        #container3
        Label(root6,text="",bg="coral1",width=2).pack(side=RIGHT)
        Lf2=Frame(root6,bg="Indianred3",width=360,height=500)
        Lf2.pack(side=RIGHT)
        Label(Lf2,text="Non-Vegetables",fg="black",bg="Indianred3",font=("mono",14,"italic")).place(x=115,y=10)
        Label(Lf2,text="-----------------------------------------------",bg="Indianred3").place(x=65,y=35)
        Label(Lf2,text="Qty.",bg="Indianred3").place(x=210,y=60)
        Label(Lf2,text="Price",bg="Indianred3").place(x=285,y=60)
        #Flesh
        Label(Lf2,text="Meat :",fg="black",bg="Indianred3",font=("mono",11,"italic")).place(x=85,y=90)
        qn1=Entry(Lf2,bd=0,width=4)
        qn1.place(x=210,y=91)
        nv1=Entry(Lf2,bd=0,width=7)
        nv1.place(x=280,y=91)
        Label(Lf2,text="Chicken :",fg="black",bg="Indianred3",font=("mono",11,"italic")).place(x=85,y=150)
        qn2=Entry(Lf2,bd=0,width=4)
        qn2.place(x=210,y=151)
        nv2=Entry(Lf2,bd=0,width=7)
        nv2.place(x=280,y=151)
        Label(Lf2,text="Beef :",fg="black",bg="Indianred3",font=("mono",11,"italic")).place(x=85,y=210)
        qn3=Entry(Lf2,bd=0,width=4)
        qn3.place(x=210,y=211)
        nv3=Entry(Lf2,bd=0,width=7)
        nv3.place(x=280,y=211)
        #Eggs&Fish
        Label(Lf2,text="Eggs :",fg="black",bg="Indianred3",font=("mono",11,"italic")).place(x=85,y=270)
        qn4=Entry(Lf2,bd=0,width=4)
        qn4.place(x=210,y=271)
        nv4=Entry(Lf2,bd=0,width=7)
        nv4.place(x=280,y=271)
        Label(Lf2,text="Fish :",fg="black",bg="Indianred3",font=("mono",11,"italic")).place(x=85,y=330)
        qn5=Entry(Lf2,bd=0,width=4)
        qn5.place(x=210,y=331)
        nv5=Entry(Lf2,bd=0,width=7)
        nv5.place(x=280,y=331)
        Label(Lf2,text="Total :",fg="black",bg="Indianred3",font=("mono",11,"italic")).place(x=210,y=387)
        t2=Entry(Lf2,bd=0,width=7)
        t2.place(x=280,y=390)
        #total
        Button(Lf2,text="Total",highlightbackground="light Grey",width=10,height=2,command=lambda: total(3)).place(x=140,y=440)

    
        #calculator
        Label(root6,text="calc :",bg="coral1",font=("mono",11)).place(x=1080,y=90)
        Button(root6,text="+/-",command=calc.calculator).place(x=1125,y=90)

        #receipt
        Button(root6,text="RECEIPT",bg="springgreen3",height=1,width=7,command=receipt).place(x=1000,y=90)
        Label(root6, text="",bg="coral1").place(x=1050,y=50)

        root6.mainloop()


