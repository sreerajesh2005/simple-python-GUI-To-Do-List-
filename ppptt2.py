import tkinter
from tkinter import *

root = Tk()
root.title("to-do-list")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task.strip() != '':
                task_list.append(task.strip())
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        with open('tasklist.txt', 'w') as file:
            file.close()


 # Top bar
TopImage = PhotoImage(file="image/topbaal.png")  # Add your file path here
Label(root,image=TopImage).pack()




heading = Label(root, text="ALL TASKS", font="arial 18 bold", fg="white", bg="#000000")
heading.place(x=130, y=20)

# Main frame
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=19, font="arial 18", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()
""
button = Button(frame, text="ADD", font="italian 20 bold", width="6", bg="#FFD700", fg="black", bd=0, command=addTask)
button.place(x=300, y=0)

frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=("jura", 12), width=40, height=13, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Delete button
Delete_icon = PhotoImage(file="image/delete.png")  # Add your delete icon file path here
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

openTaskFile()

root.mainloop()
