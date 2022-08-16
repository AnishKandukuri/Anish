from Tkinter import *
top=Tk()
lab=Label(top,text="Flavours Restaurant",fg='red')
lab.grid(row=0,column=2)
lab.config(font=('courier',10))
l1=Label(top,text="Fries ")
l1.grid(row=2,column=0)
e1=Entry(top,bd=5,bg='skyblue')
e1.grid(row=2,column=1)
fri1=Label(top,text="30/-")
fri1.grid(row=2,column=2)
l2=Label(top,text="Noodles ")
l2.grid(row=3,column=0)
e2=Entry(top,bd=5,bg='skyblue')
e2.grid(row=3,column=1)
noo1=Label(top,text="30/-")
noo1.grid(row=3,column=2)
l3=Label(top,text="Soup ")
l3.grid(row=4,column=0)
e3=Entry(top,bd=5,bg='skyblue')
e3.grid(row=4,column=1)
sou1=Label(top,text="10/-")
sou1.grid(row=4,column=2)
l4=Label(top,text="Burger ")
l4.grid(row=5,column=0)
e4=Entry(top,bd=5,bg='skyblue')
e4.grid(row=5,column=1)
bur1=Label(top,text="25/-")
bur1.grid(row=5,column=2)
l5=Label(top,text="Sandwich ")
l5.grid(row=6,column=0)
e5=Entry(top,bd=5,bg='skyblue')
e5.grid(row=6,column=1)
san1=Label(top,text="35/-")
san1.grid(row=6,column=2)
l6=Label(top,text="Drinks ")
l6.grid(row=7,column=0)
e6=Entry(top,bd=5,bg='skyblue')
e6.grid(row=7,column=1)
dri1=Label(top,text="15/-")
dri1.grid(row=7,column=2)
l7=Label(top,text="Cost of meal")
l7.grid(row=2,column=3)
e7=Entry(top,bd=5,bg='skyblue')
e7.grid(row=2,column=4)
l8=Label(top,text="Service Charge")
l8.grid(row=3,column=3)
e8=Entry(top,bd=5,bg='skyblue')
e8.grid(row=3,column=4)
sc1=Label(top,text="15%")
sc1.grid(row=3,column=5)
l9=Label(top,text="Sales Tax")
l9.grid(row=4,column=3)
e9=Entry(top,bd=5,bg='skyblue')
e9.grid(row=4,column=4)
st1=Label(top,text="5%")
st1.grid(row=4,column=5)
l10=Label(top,text="Sub Total")
l10.grid(row=5,column=3)
e10=Entry(top,bd=5,bg='skyblue')
e10.grid(row=5,column=4)

l11=Label(top,text="Total Cost")
l11.grid(row=6,column=3)
e11=Entry(top,bd=5,bg='skyblue')
e11.grid(row=6,column=4)

def add():
    if(e1.get().isdigit()):
        fri=float(e1.get())*30
    else:
        fri=0
    if(e2.get().isdigit()):
        noo=float(e2.get())*30
    else:
        noo=0
    if(e3.get().isdigit()):
        sou=float(e3.get())*10
    else:
        sou=0
    if(e4.get().isdigit()):
        bur=float(e4.get())*25
    else:
        bur=0
    if(e5.get().isdigit()):
        san=float(e5.get())*35
    else:
        san=0
    if(e6.get().isdigit()):
        dri=float(e6.get())*15
    else:
        dri=0
    e7.delete(0,END)
    com=fri+noo+sou+bur+san+dri
    e7.insert(0,com)
    sc=(com*15)/100.0
    e8.delete(0,END)
    e8.insert(0,sc)
    st=(com*5)/100.0
    e9.delete(0,END)
    e9.insert(0,st)
    sub=sc+st
    e10.delete(0,END)
    e10.insert(0,sub)
    tc=com+sub
    e11.delete(0,END)
    e11.insert(0,tc)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)

but=Button(top,text="Total",command=add)
but.grid(row=8,column=1)
b1=Button(top,text="Reset",command=clear)
b1.grid(row=8,column=2)
b2=Button(top,text="Quit",command=top.destroy)
b2.grid(row=8,column=3)
top.geometry('700x250+40+30')
top.mainloop()
