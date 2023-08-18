from tkinter import *
root = Tk()
root.geometry("350x420")
root.title("Calculator")

def click(event):
    global sc
    text=event.widget.cget("text")
    if text=="=":
        if sc.get().isdigit():
            value=int(sc.get())

        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"


        sc.set(value)
        screen.update()
    elif text=="C":
        sc.set("")
        screen.update()
    else:
        sc.set(sc.get()+text)
        screen.update()


sc=StringVar()
sc.set("")
screen=Entry(root, textvariable=sc, font="lucida 20 bold", relief=SUNKEN)
screen.grid(columnspan=4, ipadx=24, ipady=5)

b=Button(root, text='C', padx=30, pady=20)
b.grid(row=1, column=0, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='%', padx=30, pady=20)
b.grid(row=1, column=1, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='.', padx=30, pady=20)
b.grid(row=1, column=2, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='/', padx=30, pady=20)
b.grid(row=1, column=3, pady=5)
b.bind("<Button-1>",click)



b=Button(root, text='7', padx=30, pady=20)
b.grid(row=2, column=0, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='8', padx=30, pady=20)
b.grid(row=2, column=1, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='9', padx=30, pady=20)
b.grid(row=2, column=2, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='*', padx=30, pady=20)
b.grid(row=2, column=3, pady=5)
b.bind("<Button-1>",click)



b=Button(root, text='4', padx=30, pady=20)
b.grid(row=3, column=0, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='5', padx=30, pady=20)
b.grid(row=3, column=1, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='6', padx=30, pady=20)
b.grid(row=3, column=2, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='-', padx=30, pady=20)
b.grid(row=3, column=3, pady=5)
b.bind("<Button-1>",click)



b=Button(root, text='1', padx=30, pady=20)
b.grid(row=4, column=0, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='2', padx=30, pady=20)
b.grid(row=4, column=1, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='3', padx=30, pady=20)
b.grid(row=4, column=2, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='+', padx=30, pady=20)
b.grid(row=4, column=3, pady=5)
b.bind("<Button-1>",click)


b=Button(root, text='00', padx=30, pady=20)
b.grid(row=5, column=0, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='0', padx=30, pady=20)
b.grid(row=5, column=1, pady=5)
b.bind("<Button-1>",click)

b=Button(root, text='=', padx=30, pady=20, bg='orange')
b.grid(row=5, column=2, pady=5)
b.bind("<Button-1>",click)







root.mainloop()