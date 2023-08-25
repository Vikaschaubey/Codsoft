from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("390x500")
root.title('To-Do List')
root.config(bg="darkblue")

def add_task():
    task = entry.get()
    if task:
        tasks_list.insert(0,task)
        entry.delete(0,END)
        save_tasks()
    else:
        messagebox.showerror("Error","Enter a task")

def remove_task():
    selected=tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showinfo("Error", "Choose a task to delete")

def save_tasks():
    with open("to_do.txt","w") as f:
        tasks = tasks_list.get(0,END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("to_do.txt","r") as f:
            tasks = f.readlines()
            for task in tasks:
                tasks_list.insert(0,task.strip())
    except FileNotFoundError:
        messagebox.showerror("Error","Cannot load tasks")




label=Label(root,text="To-Do List",font="Arial 30 bold", fg="white", bg="darkblue")
label.grid(row=0, columnspan=5)

add_btn=Button(root, font="arial 14 bold", fg="#fff", text="Add Task", bg="#06911f", cursor="hand2",padx=20, pady=10,command=add_task)
add_btn.grid(row=2,column=1,pady=20,padx=20)

remove_btn=Button(root, font="arial 14 bold", fg="#fff", text="Remove Task", bg="#96061c", cursor="hand2",padx=10,pady=10,command=remove_task)
remove_btn.grid(row=2,column=3,pady=20,padx=20)

entry=Entry(root,font="Arial 14 bold", fg="#000", bg="#fff")
entry.grid(row=3,columnspan=5,ipadx=50,ipady=5)


tasks_list=Listbox(root,width=20,height=10,font="arial 14 bold")
tasks_list.grid(row=4,columnspan=5,ipadx=50,pady=20)



load_tasks()


root.mainloop()