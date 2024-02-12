from tkinter import *
import math
root=Tk()
root.geometry("375x471")
root.title("Calculator")
root.config(bg="grey")

var=StringVar()
var1=StringVar()
oper=["+","-","/","*","x"]
operator=""
ls=["%","c",chr(9249),"()","x"+chr(178),"y"+chr(5501),chr(8730),"/",7,8,9,"x",4,5,6,"-",1,2,3,"+","!",0,".","="]
for i in range(len(ls)):
    ls[i]=str(ls[i])

display=Label(root,bg="white",fg="grey",textvariable=var1,font="lucida 15 bold",anchor=NE,padx=10,pady=4)
display.place(x=3,y=3,height=30,width=369)
display=Label(root,bg="white",textvariable=var,font="lucida 35 bold",anchor=SE,padx=6,pady=3)
display.place(x=3,y=33,height=57,width=369)


def fibonachi(n):
    if n==1:
        return n
    else:
        return n*fibonachi(n-1)
def percentfun(n):
    n=n.replace("%","")
    i=operator
    ls=n.rsplit(i,1)
    value=eval(ls[0])
    num=int(ls[1])
    if i=="+":
        return value+value*num/100
    elif i=="-":
        return value-value*num/100
    elif i=="*"or i=="x":
        return value*num/100
    elif i=="/":
        return value/(num/100)
def bracket():
    a=var.get()
    for i in range(0,10):
        if a.__contains__("(") and a[-1]!=("("):
            var.set(a+")")
        elif a[-1]==str(i):
            var.set(a+"x"+"(")
        else:
            var.set(a+"(")
def calc_fun(text):
    a=var.get()
    global operator
    try:
        if text=='=' or text=="\r": 
            try:
                var1.set(a)
                if a[-1]=="%":
                    var.set(percentfun(a))
                elif a[-1]=="!":
                    a=a.removesuffix(a[-1])
                    var.set(fibonachi(int(a)))
                elif a.__contains__(chr(8730)): #for sqare root
                    a=a.split(chr(8730))
                    a=round(eval(a[0]+str(math.sqrt(int(a[1])))),4)
                    var.set(a)
                else:
                    a=a.replace("x","*")
                    a=a.replace("^","**")
                    var.set(eval(a))      
            except:
                var.set("Error")  
        
        elif text in oper and a[-1] in oper:
            var.set(a.removesuffix(a[-1])+text)
            operator=text
        elif text=="c":
            var.set("")
            var1.set("")
        elif text==chr(9249) or text=="\x08": #Back space
            var.set(a.removesuffix(a[-1]))
        elif text=="()":
            bracket()
        elif text==("x"+chr(178)): #sqare 
            var.set(a+"^"+"2")
        elif text=="y"+chr(5501): #y to the power x
            var.set(a+"^")
        else:
            var.set(var.get()+text)
            if text in oper:
                operator=text
    except:
        if text=="()":
            bracket()
        else:
            var.set(a+text)
            if text in oper:
                    operator=text 


def kill(event):
    text=event.char
    calc_fun(text)
       
root.bind('<Key>',kill)
root.bind("<Delete>",lambda event:(var.set(""),var1.set("")))



def effect(event):
    event.widget.config(bg="#18E751",fg="white",font=("Helvetica",30))
def effect1(event):
    event.widget.config(bg="white",fg="black",font=("Helvetica",20))
def click(event):
    text=event.widget.cget("text")
    calc_fun(text)
    
def buttons(num,X,Y):    
    button=Label(root,text=num,bg="white",font=("Helvetica",20))
    button.place(x=X,y=Y,height=60,width=90) 
    button.bind("<Motion>",effect)
    button.bind("<Leave>",effect1)
    button.bind('<Button-1>',click)
    
def list():
    X=3
    Y=93    
    for num in ls:
        buttons(num,X,Y)
        X+=93
        if X==375:
            Y+=63
            X=3


list()
root.mainloop()
