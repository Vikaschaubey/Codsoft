from tkinter import *
import random, string

root=Tk()
root.geometry("750x600")
root.title("Random Password Generator")

def callback():
    lsum.config(text=passgen())

def passgen():
    global a
    a = "".join(random.sample(adv,lenvalue.get()))
    return a

def accept():
    print(f"Name => {namevalue.get()}")
    print(f"Password => {a}")

def reset():
    namevalue.set("")
    lenvalue.set("")
    lsum.config(text="")

label=Label(root, text="Password Generator", fg="blue", font="comicsansms 30 bold underline", pady=15).grid(row=0,column=3)

name=Label(root,text="Enter user name:", font="lucida 18 bold",padx=20,pady=25).grid(row=1,column=2)
length=Label(root,text="Enter Password length:", font="lucida 18 bold",padx=20,pady=25).grid(row=2,column=2)
password=Label(root,text="Generated password:", font="lucida 18 bold",padx=20,pady=25).grid(row=3,column=2)

namevalue=StringVar()
namevalue.set("")

lenvalue=IntVar()
lenvalue.set("")

passvalue=StringVar()
passvalue.set("")


nameentry=Entry(root,textvariable=namevalue, font="lucida 20",borderwidth=1,highlightthickness=2,relief=GROOVE).grid(row=1,column=3,ipadx=20,ipady=5)
lenentry=Entry(root,textvariable=lenvalue, font="lucida 20",borderwidth=1,highlightthickness=2,relief=GROOVE).grid(row=2,column=3,ipadx=20,ipady=5)
passentry=Label(root,textvariable=passvalue, font="lucida 20 bold",borderwidth=1,highlightthickness=2,relief=GROOVE, padx=150).grid(row=3,column=3,ipadx=20,ipady=5)

pbtn=Button(root, text="GENERATE PASSWORD",command=callback, font="lucida 17 bold", bg="darkblue",fg="white", padx=10, pady=2, borderwidth=4, highlightthickness=4, relief=GROOVE)
pbtn.grid(row=4,column=3,pady=20)

pasword=str(callback)

lsum=Label(root,text="", font="lucida 18 bold")
lsum.grid(row=3,column=3)

symbol="""~!@#$%^&*()_+`,./;'[]<>?:}{"""
adv=string.ascii_uppercase+string.ascii_lowercase+string.digits+symbol


Button(root,text="ACCEPT", command=accept, font="lucida 17", bg="white", fg="darkblue", padx=25, pady=2, borderwidth=4, highlightthickness=4, relief=GROOVE).grid(row=5, column=3,pady=10)

Button(root,text="RESET", command=reset, font="lucida 17", bg="white", fg="darkblue", padx=25, pady=2, borderwidth=4, highlightthickness=4, relief=GROOVE).grid(row=6, column=3,pady=10)

root.mainloop()