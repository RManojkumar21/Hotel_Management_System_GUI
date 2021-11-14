from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
import pymysql

con=pymysql.connect(host="localhost",user="root",password='',database='Hotel Management')

a,c=0,0
k=0

def addRoom():
    Name=name.get()
    Phone=phone.get()
    Roomno=roomno.get()
    Meals=meals.get()
    Roomtype=roomtype.get()
    Checkin=checkin.get()
    Checkout=checkout.get()
    cur=con.cursor()
    room = (
                   "INSERT INTO Room(NAME, PHONENO, ROOMNO, MEALS, ROOMTYPE, CHECKIN, CHECKOUT)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)"
           )
    if Name=="" or Phone=="" or Roomno=="" or Meals=="" or Roomtype=="" or Checkin=="" or Checkout=="":
        messagebox.showerror("Error","Field is Empty !")
    else:
        a=messagebox.askyesno("Confirm","Confirm ?")
        if a==1:
            data=(Name, Phone, Roomno, Meals, Roomtype, Checkin, Checkout)
            try:
                #executing the sql command
                cur.execute(room,data)
                #commit changes in database
                con.commit()
                messagebox.showinfo("Success","Stored Successfully")
            except:
                con.rollback()
        else:
            return


def clear():
    s=""
    return name.delete(0,END),phone.delete(0,END),roomno.delete(0,END),meals.set(''),roomtype.set(''),checkin.delete(0,END),checkout.delete(0,END)

def calendar():
    global Lf,c,cal,btn
    c+=1
    
    if c%2!=0:
        cal=Calendar(Lf, selectmode='day',year=2021,month=7,day=20)
        cal.place(x=520,y=160)
        def date():
            global c
            c=0
            a=cal.get_date()
            checkin.delete(0,END)
            checkin.insert(0,a)
            cal.destroy()
            btn.place(x=1000,y=550)
            
        btn=Button(Lf,text="Date",bd=0,command=date)
        btn.place(x=615,y=320)
        
    else:
        cal.destroy()
        btn.place(x=1000,y=550)

def calendar1():
    global Lf,a,cal1,btn1,cal,btn,c,checkin
    chk=checkin.get()
    if chk=="":
        messagebox.showerror("Warning","First Select CheckIn !")
    else:
            cal.destroy()
            btn.place(x=1000,y=550)
            c=0
            a+=1
            if a%2!=0:
                cal1=Calendar(Lf, selectmode='day',year=2021,month=7,day=20)
                cal1.place(x=520,y=220)
                def date():
                    global a
                    a=0
                    d=cal1.get_date()
                    checkout.delete(0,END)
                    checkout.insert(0,d)
                    cal1.destroy()
                    btn1.place(x=1000,y=550)
                    
                btn1=Button(Lf,text="Date",bd=0,command=date)
                btn1.place(x=615,y=380)
        
            else:
                cal1.destroy()
                btn1.place(x=1000,y=550)
                
        
def exit():
    "dummy function"
    pass           
 
def room():
    global name,phone,roomno,meals,roomtype
    global Lf,checkin,checkout
    global k
    k+=1
    if k==1:
        root7=Toplevel()
        root7.title("Room Section")
        root7.resizable(False,False)
        root7.geometry("1000x700")
        root7.protocol("WM_DELETE_WINDOW",exit)
        root7.configure(bg="sandybrown")
        Label(root7,text="",bg="sandybrown").pack()
        Label(root7,text="ROOM INFO",bg="light Grey",fg="Black",font=("ubuntu",30,"italic"),width=12).pack()
        Label(root7,text="",bg="sandybrown",height=3).pack()

        meals=StringVar()
        roomtype=StringVar()


        #back
        def back():
            global k
            a=messagebox.askyesno("Warning!","Do you want to go back ?")
            if a==1:
                k=0
                root7.destroy()
            else:
                return
            
        Label(root7,text="",bg="sandybrown").pack(side=BOTTOM)
        Button(root7,text="back",highlightbackground="light Grey",fg="black",width=6,height=2,command=back).place(x=900,y=630)
        #container
        Lf=Frame(root7,bg="tan3",width=750,height=500)
        Lf.pack()

        #Name
        Label(Lf,text="Name :",bg="tan3",fg="black",font=("ubuntu",17,"italic")).place(x=200,y=20)
        name=Entry(Lf,bd=0)
        name.place(x=320,y=22)

        #Phone_no.
        Label(Lf,text="Phone No :",bg="tan3",fg="black",font=("ubuntu",17,"italic")).place(x=200,y=80)
        phone=Entry(Lf,bd=0)
        phone.place(x=320,y=82)

        #Room_No.
        Label(Lf,text="Room No :",bg="tan3",fg="black",font=("ubuntu",17,"italic")).place(x=200,y=140)
        roomno=Entry(Lf,bd=0)
        roomno.place(x=320,y=142)

        #Meals
        Label(Lf,text="Meals :",bg="tan3",fg="black",font=("ubuntu",17,"italic")).place(x=200,y=200)
        meals=ttk.Combobox(Lf,width=18)
        meals["values"]=('Taken','Not Taken')
        meals["state"]='readonly'
        meals.place(x=320,y=202)

        #Room_Type
        Label(Lf,text="Room Type :",bg="tan3",fg="black",font=("ubuntu",17,"italic")).place(x=200,y=260)
        roomtype=ttk.Combobox(Lf,width=18)
        roomtype["values"]=('Single Room','Double Room','Deluxe')
        roomtype["state"]='readonly'
        roomtype.place(x=320,y=262)
        #check_in
        Label(Lf,text="Check In :",bg="tan3",fg="black",font=("ubuntu",17,"italic")).place(x=200,y=320)
        checkin=Entry(Lf,bd=0)
        checkin.place(x=320,y=322)

        #check_out
        Label(Lf,text="Check Out :",bg="tan3",fg="black",font=("ubuntu",17,"italic")).place(x=200,y=380)
        checkout=Entry(Lf,bd=0)
        checkout.place(x=320,y=382)

        #add
        Button(Lf,text="Add",highlightbackground="tan1",width=10,height=2,command=addRoom).place(x=270,y=440)
        #clear
        Button(Lf,text="Clear",highlightbackground="tan1",width=10,height=2,command=clear).place(x=370,y=440)    
        #calendar
        Button(Lf,text="-|||-",highlightbackground="tan3",command=calendar).place(x=515,y=323)
        Button(Lf,text="-|||-",highlightbackground="tan3",command=calendar1).place(x=515,y=383)    
    
        root7.mainloop()
    
