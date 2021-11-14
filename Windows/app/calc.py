#calculator_app
from tkinter import *
from tkinter import messagebox
import math


c=0
def press(a):
        global s
        s=str(a)
        e.insert(END,s)


def func(o):
        global s
        s=o
        e.insert(END,s)
       

def equal():
        global s
        eq=e.get()
        try:
                a=eval(eq)
                x,y=math.modf(a)
                if x==0.0:
                        e.delete(0,END)
                        s=str(int(a))
                        e.insert(0,s)
                else:
                        e.delete(0,END)
                        s=str(a)
                        e.insert(0,s)
        except:
                messagebox.showerror("Error","Error")
        


def delete():
        eq=e.get()
        s=len(eq)
        e.delete(s-1,s)


def clear1():
        e.delete(0,END)



def calculator():
        global equal,clear,delete,e,calc
        
        calc=Toplevel()
        calc.title("Calculator")
        calc.geometry("263x320")
        calc.configure(bg="grey")
        calc.resizable(False,False)        

        e=Entry(calc,bd=5,width=42,fg="white",bg="black",insertbackground="white")
        e.grid(columnspan=10,ipady=7)
        e.focus_set()
        
    
        n1=Button(calc,text="1",fg="white",bg="grey10",width=8,height=3,command=lambda: press(1))
        n1.grid(row=3,column=0)   
        n2=Button(calc,text="2",fg="white",bg="grey10",width=8,height=3,command=lambda: press(2)) 
        n2.grid(row=3,column=1)
        n3=Button(calc,text="3",fg="white",bg="grey10",width=8,height=3,command=lambda: press(3))
        n3.grid(row=3,column=2)
        add=Button(calc,text="+",fg="white",bg="goldenrod1",width=8,height=3,command=lambda: func("+"))
        add.grid(row=3,column=3)

        n4=Button(calc,text="4",fg="white",bg="grey10",width=8,height=3,command=lambda: press(4))
        n4.grid(row=4,column=0)
        n5=Button(calc,text="5",fg="white",bg="grey10",width=8,height=3,command=lambda: press(5))
        n5.grid(row=4,column=1)
        n6=Button(calc,text="6",fg="white",bg="grey10",width=8,height=3,command=lambda: press(6))
        n6.grid(row=4,column=2)
        sub=Button(calc,text="-",fg="white",bg="goldenrod1",width=8,height=3,command=lambda: func("-"))
        sub.grid(row=4,column=3)

        n7=Button(calc,text="7",fg="white",bg="grey10",width=8,height=3,command=lambda: press(7))
        n7.grid(row=5,column=0)
        n8=Button(calc,text="8",fg="white",bg="grey10",width=8,height=3,command=lambda: press(8))
        n8.grid(row=5,column=1)
        n9=Button(calc,text="9",fg="white",bg="grey10",width=8,height=3,command=lambda: press(9))
        n9.grid(row=5,column=2)
        multi=Button(calc,text="*",fg="white",bg="goldenrod1",width=8,height=3,command=lambda: func("*"))
        multi.grid(row=5,column=3)

        n0=Button(calc,text="0",fg="white",bg="grey10",width=8,height=3,command=lambda: press(0))
        n0.grid(row=6,column=0)
        deci=Button(calc,text=".",fg="white",bg="grey10",width=8,height=3,command=lambda: press("."))
        deci.grid(row=6,column=1)
        equal=Button(calc,text="=",fg="white",bg="grey10",width=8,height=3,command=equal)
        equal.grid(row=6,column=2)
        div=Button(calc,text="/",fg="white",bg="goldenrod1",width=8,height=3,command=lambda: func("/"))
        div.grid(row=6,column=3)

        lbrace=Button(calc,text="(",fg="white",bg="goldenrod1",width=8,height=3,command=lambda: press("("))
        lbrace.grid(row=7,column=2)
        rbrace=Button(calc,text=")",fg="white",bg="goldenrod1",width=8,height=3,command=lambda: press(")"))
        rbrace.grid(row=7,column=3)
        delete=Button(calc,text="del",fg="white",bg="red",width=8,height=3,command=delete)
        delete.grid(row=7,column=1)
        clear=Button(calc,text="C",fg="white",bg="green",width=8,height=3,command=clear1)
        clear.grid(row=7,column=0)

        calc.mainloop()

