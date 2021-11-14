from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql

#connection to database
con = pymysql.connect(user='root', password='', host='localhost', database='Hotel Management')
c=0

x,y,z,e=0,0,0,0

x1,y1,z1,e1=0,0,0,0

k,m=0,0

def gen(n):
    global gender
    if n==1:
        gender=n
    else:
        gender=n

def check(a):
    global x,y,z,e,x1,y1,z1,e1
    if a==1:
        x1+=1
        if x1%2!=0:
            x=a
        else:
            x=0
    elif a==2:
        y1+=1
        if y1%2!=0:
            y=a
        else:
            y=0
    elif a==3:
        z1+=1
        if z1%2!=0:
            z=a
        else:
            z=0
    elif a==4:
        e1+=1
        if e1%2!=0:
            e=a
        else:
            e=0

        
def status(m):
    global stat
    if m==1:
        stat=m
    else:
        stat=m
        

def addEmployee():
    try:
        Name=name.get()
        Age=age.get()
        Dob=dob.get()
        Gender=gender
        Contact=contact.get()
        Email=mail.get()
        Address=address.get()
        City=city.get()
        State=state.get()
        Department=dep.get()
        Status=stat
        EmploymentType=emptype.get()
        Salary=salary.get()
        a=x
        b=y
        c=z
        d=e
    except:
            messagebox.showerror("Error","Please Select Important Field")
            return
        
    #Inserting data to mysql        
    if Name==""or Age==""or Dob=="" or Contact==""or Email==""or Address==""or City==""or State==""or Department==""or EmploymentType==""or Salary=="":
        messagebox.showerror("Error","Field is Empty")
    else:
        cur = con.cursor()
        add_employee=(
                "INSERT INTO Employee(NAME, AGE, DOB, GENDER, CONTACT, EMAIL, ADDRESS, CITY, STATE, DEPARTMENT, STATUS, IDPROOF, TYPE, SALARY)" 
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                )

        if Gender==1 and Status==1:
            if a==1 and b==2 and c==3 and d==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/PAN/Passport", EmploymentType, Salary)
            elif a==1 and c==3 and d==4 and b==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/Passport/DL", EmploymentType, Salary)
            elif a==1 and b==2 and d==4 and c==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/PAN/DL", EmploymentType, Salary)
            elif b==2 and c==3 and d==4 and a==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Active", "PAN/Passport/DL", EmploymentType, Salary)
            else:
                messagebox.showinfo("Error","Select Any 3 Id-Proof")
                return
            
        elif Gender==1 and Status==2:
            if a==1 and b==2 and c==3 and d==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/PAN/Passport", EmploymentType, Salary)
            elif a==1 and c==3 and d==4 and b==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/Passport/DL", EmploymentType, Salary)
            elif a==1 and b==2 and d==4 and c==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/PAN/DL", EmploymentType, Salary)
            elif b==2 and c==3 and d==4 and a==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Inactive", "PAN/Passport/DL", EmploymentType, Salary)
            else:
                messagebox.showinfo("Error","Select Any 3 Id-Proof")
                return


        elif Gender==2 and Status==1:
            if a==1 and b==2 and c==3 and d==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/PAN/Passport", EmploymentType, Salary)
            elif a==1 and c==3 and d==4 and b==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/Passport/DL", EmploymentType, Salary)
            elif a==1 and b==2 and d==4 and c==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/PAN/DL", EmploymentType, Salary)
            elif b==2 and c==3 and d==4 and a==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Active", "PAN/Passport/DL", EmploymentType, Salary)
            else:
                messagebox.showinfo("Error","Select Any 3 Id-Proof")
                return


        elif Gender==2 and Status==2:
            if a==1 and b==2 and c==3 and d==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/PAN/Passport", EmploymentType, Salary)
            elif a==1 and c==3 and d==4 and b==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/Passport/DL", EmploymentType, Salary)
            elif a==1 and b==2 and d==4 and c==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/PAN/DL", EmploymentType, Salary)
            elif b==2 and c==3 and d==4 and a==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Inactive", "PAN/Passport/DL", EmploymentType, Salary)
            else:
                messagebox.showinfo("Error","Select Any 3 Id-Proof")
                return
        else:
                messagebox.showerror("Error","Please Select Important Field")
                return
    

        try:
            a=messagebox.askyesno("Confirm","Confirm ?")
            if a==1:
                #executing the sql command
                cur.execute(add_employee,data)
                #commit changes in database
                con.commit()
                messagebox.showinfo("Success","Stored Successfully")
                reset()
            else:
                return
        except:
            con.rollback()
            messagebox.showinfo("Error","Please Enter Valid Details")

def updateEmployee():
    try:
        Name=name.get()
        Age=age.get()
        Dob=dob.get()
        Gender=gender
        Contact=contact.get()
        Email=mail.get()
        Address=address.get()
        City=city.get()
        State=state.get()
        Department=dep.get()
        Status=stat
        EmploymentType=emptype.get()
        Salary=salary.get()
        a=x
        b=y
        c=z
        d=e
        print(a,b,c,d)
    except:
            messagebox.showerror("Error","Please Select Important Field")
            return
        
    #Inserting data to mysql        
    if Name==""or Age==""or Dob=="" or Contact==""or Email==""or Address==""or City==""or State==""or Department==""or EmploymentType==""or Salary=="":
        messagebox.showerror("Error","Field is Empty")
    else:

        if Gender==1 and Status==1:
            if a==1 and b==2 and c==3 and d==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/PAN/Passport", EmploymentType, Salary)
            elif a==1 and c==3 and d==4 and b==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/Passport/DL", EmploymentType, Salary)
            elif a==1 and b==2 and d==4 and c==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/PAN/DL", EmploymentType, Salary)
            elif b==2 and c==3 and d==4 and a==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Active", "PAN/Passport/DL", EmploymentType, Salary)
            else:
                messagebox.showinfo("Error","Select Any 3 Id-Proof")
                return
            
        elif Gender==1 and Status==2:
            if a==1 and b==2 and c==3 and d==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/PAN/Passport", EmploymentType, Salary)
            elif a==1 and c==3 and d==4 and b==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/Passport/DL", EmploymentType, Salary)
            elif a==1 and b==2 and d==4 and c==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/PAN/DL", EmploymentType, Salary)
            elif b==2 and c==3 and d==4 and a==0:
                data=(Name, Age, Dob, "Male", Contact, Email, Address, City, State, Department, "Inactive", "PAN/Passport/DL", EmploymentType, Salary)
            else:
                messagebox.showinfo("Error","Select Any 3 Id-Proof")
                return


        elif Gender==2 and Status==1:
            if a==1 and b==2 and c==3 and d==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/PAN/Passport", EmploymentType, Salary)
            elif a==1 and c==3 and d==4 and b==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/Passport/DL", EmploymentType, Salary)
            elif a==1 and b==2 and d==4 and c==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Active", "Aadhaar/PAN/DL", EmploymentType, Salary)
            elif b==2 and c==3 and d==4 and a==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Active", "PAN/Passport/DL", EmploymentType, Salary)
            else:
                messagebox.showinfo("Error","Select Any 3 Id-Proof")
                return


        elif Gender==2 and Status==2:
            if a==1 and b==2 and c==3 and d==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/PAN/Passport", EmploymentType, Salary)
            elif a==1 and c==3 and d==4 and b==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/Passport/DL", EmploymentType, Salary)
            elif a==1 and b==2 and d==4 and c==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Inactive", "Aadhaar/PAN/DL", EmploymentType, Salary)
            elif b==2 and c==3 and d==4 and a==0:
                data=(Name, Age, Dob, "Female", Contact, Email, Address, City, State, Department, "Inactive", "PAN/Passport/DL", EmploymentType, Salary)
            else:
                messagebox.showinfo("Error","Select Any 3 Id-Proof")
                return
        else:
                messagebox.showerror("Error","Please Select Important Field")
                return

        #Updating data to mysql
        l=data
        print(Mobile)
        cur=con.cursor()
        update=("UPDATE Employee SET NAME='"+l[0]+"',AGE='"+l[1]+"',DOB='"+l[2]+"',GENDER='"+l[3]+"',CONTACT='"+l[4]+"',EMAIL='"+l[5]+"',ADDRESS='"+l[6]+"',CITY='"+l[7]+"',STATE='"+l[8]+"',DEPARTMENT='"+l[9]+"',STATUS='"+l[10]+"',IDPROOF='"+l[11]+"',TYPE='"+l[12]+"',SALARY='"+l[13]+"' where CONTACT='"+Mobile+"'")
        a=messagebox.askyesno("Confirm","Are you Sure\nYou want to Update ?")
        if a==1:
            try:
                #executing the sql command
                cur.execute(update)
                #commit changes in database
                con.commit()
                messagebox.showinfo("Success","Updated Successfully!")
                reset()
            except:
                con.rollback()
                messagebox.showinfo("Error","Please Enter Valid Details")
            
        

def update():
    global root5,c
    if c%2==0:
        rootsub6=Toplevel(root5)
        rootsub6.resizable(False,False)
        rootsub6.geometry("400x200")
        rootsub6.title("Update Employee")
        rootsub6.configure(bg="springgreen2")
        Label(rootsub6,text="",bg="springgreen2").pack()
        Label(rootsub6,text="Enter Phone No. to update Employee Record :",bg="springgreen2",font=("Times new roman",14)).pack()
        Label(rootsub6,text="",bg="springgreen2").pack()
        def fetch():
            global c,root5,Mobile
            Mobile=phoneno.get()
            cur=con.cursor()
            getall="select * from Employee where CONTACT = '"+Mobile+"'"
            results=cur.execute(getall)
            l=[]
            if results:
                for i in cur:
                    for j in i:
                        l.append(j)
                c+=1
                messagebox.showinfo("Fetched","Fetched Record!")
                rootsub6.destroy()
                return name.insert(0,l[0]),age.insert(0,l[1]),dob.insert(0,l[2]),contact.insert(0,l[4]),mail.insert(0,l[5]),address.insert(0,l[6]),city.insert(0,l[7]),state.insert(0,l[8]),dep.insert(0,l[9]),emptype.insert(0,l[12]),salary.insert(0,l[13])
            else:
                c=0
                messagebox.showerror("Error","Invalid Phone No.")

        phoneno=Entry(rootsub6,bd=3,width=35)
        phoneno.pack()
        Label(rootsub6,text="",bg="springgreen2",height=2).pack()
        Button(rootsub6,text="Fetch",height=1,width=10,command=fetch).pack()
        
    else:
        updateEmployee()


def delEmployee():
    global k
    Name=nam.get()
    Phone=phone.get()
    Emp="Employee"
    
    if Name=="" or Phone=="":
        messagebox.showinfo("Error","Please Fill Both Fields")
    else:
        #delete data from database
        cur=con.cursor()
        delete="delete from "+Emp+" where NAME = '"+Name+"' and CONTACT = '"+Phone+"'"
        a=messagebox.askyesno("Confirm","Do you want to delete Employee Record ?")
        if a==1:
            results=cur.execute(delete)
            con.commit()
            if results:
                messagebox.showinfo("Success","Employee Record Deleted Successfully")
                k=0
                rootsub5.destroy()
            else:
                messagebox.showinfo("Failure","There is no matching Employee Record to delete !")                
        else:
            return
    

def delete():
    global root5,nam,phone,rootsub5,k
    k+=1
    def exit():
        "dummy function"
        pass 
    if k==1:
        rootsub5=Toplevel(root5)
        rootsub5.resizable(False,False)
        rootsub5.protocol("WM_DELETE_WINDOW",exit)
        rootsub5.geometry("400x350")
        rootsub5.title("Delete Employee")
        rootsub5.configure(bg="Indianred")
        Label(rootsub5,text="",bg="Indianred").pack()
        Label(rootsub5,text="Name:",bg="Indianred",font=("times new roman",15,"bold")).pack()
        Label(rootsub5,text="",bg="Indianred").pack()
        nam=Entry(rootsub5,bd=2,width=35)
        nam.pack()
        Label(rootsub5,text="",bg="Indianred").pack()
        Label(rootsub5,text="Contact:",bg="Indianred",font=("times new roman",15,"bold")).pack()
        Label(rootsub5,text="",bg="Indianred").pack()
        phone=Entry(rootsub5,bd=2,width=35)
        phone.pack()
        Label(rootsub5,text="",bg="Indianred").pack()
        Button(rootsub5,text="Delete",width=12,height=2,bd=3,command=delEmployee).place(x=95,y=240)
        def destroy():
            global rootsub5,k
            k=0
            rootsub5.destroy()
            
        Button(rootsub5,text="Quit",width=12,height=2,bd=3,command=destroy).place(x=205,y=240)    
    
    
  
def reset():
    global c,root5
    c=0
    s=""
    return name.delete(0,END),age.delete(0,END),dob.delete(0,END),contact.delete(0,END),mail.delete(0,END),address.delete(0,END),city.set(''),state.set(''),dep.delete(0,END),emptype.delete(0,END),salary.delete(0,END)

def exit():
    "dummy function"
    pass 

def employee():
    global name
    global age
    global dob
    global contact
    global mail
    global address
    global city
    global state
    global dep
    global emptype
    global salary
    global checkbt1
    global checkbt2
    global checkbt3
    global checkbt4
    global cy
    global st
    global root5
    global m
    m+=1
    if m==1:
        root5=Toplevel()
        root5.title("Employee Section")
        root5.resizable(False,False)
        root5.geometry("1000x700")
        root5.protocol("WM_DELETE_WINDOW",exit)
        root5.configure(bg="peachpuff1")
        Label(root5,text="",bg="peachpuff1").pack()
        Label(root5,text="EMPLOYEE INFO",bg="light Grey",fg="Black",font=("ubuntu",21,"italic"),width=15).pack()
        Label(root5,text="",bg="peachpuff1",height=3).pack()
    
        #back
        def back():
            global m
            a=messagebox.askyesno("Warning!","Do you want to go back!")
            if a==1:
                m=0
                root5.destroy()
            else:
                return
        Button(root5,bd=3,bg="White",width=6,fg="Black",font=("mono",8,"bold"),text="Back",command=back).place(x=900,y=630)
        #container
        Lf=Frame(root5,bg="springgreen2",width=700,height=500)
        Lf.pack()
    
        gender1=IntVar()
        status1=IntVar()
        c1=IntVar()
        c2=IntVar()
        c3=IntVar()
        c4=IntVar()
        cy=StringVar()
        st=StringVar()
    
        #Name
        Label(Lf,text="Name :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=10,y=20)
        name=Entry(Lf,bd=2,width=28)
        name.place(x=75,y=21)
        #Age
        Label(Lf,text="Age :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=300,y=20)
        age=Entry(Lf,bd=2,width=5)
        age.place(x=350,y=21)
        #D.O.B
        Label(Lf,text="D.O.B :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=450,y=20)
        dob=Entry(Lf,bd=2,width=15)
        dob.place(x=520,y=21)
    
        #Gender
        Label(Lf,text="Gender :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=10,y=80)
        g1=Radiobutton(Lf,text="Male",bg="springgreen2",value=1,variable=gender1,command=lambda :gen(1))
        g1.place(x=90,y=83)
        g2=Radiobutton(Lf, text="Female", bg="springgreen2",value=2,variable=gender1,command=lambda :gen(2))
        g2.place(x=150, y=83)
        #Contact
        Label(Lf,text="Contact :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=240,y=80)
        contact=Entry(Lf,bd=2,width=14)
        contact.place(x=320,y=83)
        #E-mail
        Label(Lf,text="E-mail :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=430,y=80)
        mail=Entry(Lf,bd=2,width=28)
        mail.place(x=500,y=83)
    
        #Address
        Label(Lf,text="Address :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=10,y=140)
        address=Entry(Lf,bd=2,width=35)
        address.place(x=93,y=143)
        #City
        Label(Lf,text="City :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=360,y=140)
        city=ttk.Combobox(Lf,width=11,height=5,textvariable=cy)
        city['values'] = (' Bangalore',
                                  ' Mumbai',
                                  ' Delhi',
                                  ' Chennai',
                                  ' Trivandur',
                                  ' Hyderabad',
                                  ' Pune',
                                  ' Kolkatta',
                                  ' Chandigarh',)
    
        city['state'] = 'readonly'
        city.place(x=410,y=141)
    
        #State
        Label(Lf,text="State :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=510,y=140)
        state=ttk.Combobox(Lf,width=11,height=5,textvariable=st)
        state['values'] = (' Karnatakka',
                                  ' Kerala',
                                  ' Maharashtra',
                                  ' Tamil Nadu',
                                  ' Andhra Pradhesh',
                                  ' West Bengal',
                                  ' New Delhi',
                                  ' Punjab',)
    
        state['state'] = 'readonly'
        state.place(x=570,y=141)

        #Department
        Label(Lf,text="Department :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=10,y=200)
        dep=Entry(Lf,bd=2,width=35)
        dep.place(x=120,y=202)
        #Status
        Label(Lf,text="Status :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=420,y=200)
        s1=Radiobutton(Lf,text="active",bg="springgreen2",value=1,variable=status1,command= lambda: status(1))
        s1.place(x=500,y=201)
        s2=Radiobutton(Lf, text="inactive", bg="springgreen2",value=2,variable=status1,command= lambda: status(2))
        s2.place(x=580, y=201)

        #ID_Proof
        Label(Lf,text="ID-Proof :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=10,y=260)
        checkbt1=Checkbutton(Lf,text="Aadhaar",bg="springgreen2",variable=c1,bd=0,onvalue=1,offvalue=0,command=lambda: check(1))
        checkbt1.place(x=100,y=263)
        checkbt2=Checkbutton(Lf,text="PAN Card",bg="springgreen2",variable=c2,onvalue=1,offvalue=0,bd=0,command=lambda: check(2))
        checkbt2.place(x=100,y=290)
        checkbt3=Checkbutton(Lf,text="Passport",bg="springgreen2",variable=c3,onvalue=1,offvalue=0,bd=0,command=lambda: check(3))
        checkbt3.place(x=100,y=320)
        checkbt4=Checkbutton(Lf,text="Driving Lisence",bg="springgreen2",variable=c4,onvalue=1,offvalue=0,bd=0,command=lambda: check(4))
        checkbt4.place(x=100,y=350)
        Label(Lf,text="(Any 3)",bg="springgreen2",fg="black",font=("times new roman",12,"bold")).place(x=220,y=349)

        #Employment_type
        Label(Lf,text="Employment Type :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=270,y=260)
        emptype=Entry(Lf,bd=2,width=36)
        emptype.place(x=430,y=262)
        #Salary
        Label(Lf,text="Salary :",bg="springgreen2",fg="black",font=("times new roman",13,"bold")).place(x=315,y=320)
        salary=Entry(Lf,bd=2,width=30)
        salary.place(x=395,y=322)    

        #Add,Update,Delete,Reset
        Button(Lf,text="Add",bg="royalblue3",fg="white",width=17,height=2,bd=2,command=addEmployee).place(x=58,y=420)
        Button(Lf,text="Update",bg="springgreen4",fg="white",width=17,height=2,bd=2,command=update).place(x=205,y=420)
        Button(Lf,text="Delete",bg="brown2",fg="white",width=17,height=2,bd=2,command=delete).place(x=352,y=420)
        Button(Lf,text="Reset",bg="goldenrod1",fg="white",width=17,height=2,bd=2,command=reset).place(x=499,y=420)
    
        root5.mainloop()

