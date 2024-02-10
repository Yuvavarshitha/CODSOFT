import tkinter as tk
from tkinter import *
#Show no of completed task
#show no of pending task

taskList = []
completedTasks = []
info = {"Pending Tasks":len(taskList),"Completed Tasks":len(completedTasks) }

def update():
    info["Pending Tasks"] = len(taskList)
    info["Completed Tasks"] = len(completedTasks)
    msg.configure(text= f"Pending Tasks: \t{info['Pending Tasks']} \nCompleted Tasks: {info['Completed Tasks']}")

def addTask():
    #function that executes when the current task is completed 
    def comTask():
        taskList.remove(task)
        info["Pending Tasks"] = len(taskList)
        completedTasks.append(task)
        info["Completed Tasks"] = len(completedTasks)
        #comlabel = tk.Label(info, text="task", font=("bold"))
        taskframe.destroy()
        update()

    def delTask():
        taskList.remove(task)
        info["Pending Tasks"] = len(taskList)
        taskframe.destroy()
        update()

    task = newtaskEnt.get()
    taskList.append(task)
    newtaskEnt.delete(0,tk.END)

    taskframe = tk.Frame(f2, relief=tk.RIDGE, borderwidth=3, width=100, bg="#252422")
    taskframe.pack(side=tk.TOP, fill="x") #fill='x' is used to utilize the entire available width left after allocating space for the widgets

    new_task = tk.Label(taskframe, text=task, fg="white", bg="#252422", font=("bold"))
    new_task.pack(side=tk.LEFT, fill="x")

    del_btn = tk.Button(taskframe, text="Delete", bg="red", fg="black", command=delTask)
    del_btn.pack(side=tk.RIGHT)
    com_btn = tk.Button(taskframe, text="Complete", bg="green", fg="black", command=comTask)
    com_btn.pack(side=tk.RIGHT)
    update()

window = tk.Tk()

#Organize the frames inside the window using the grid geometry manager
#the window will have Two Frames
window.rowconfigure(0, minsize=200, pad=2, weight=1)
window.columnconfigure([0,1], minsize=300, pad=2, weight=1)

#FRAME1
#frame that inputs a new task and adds it to task list and displays details
f1 = tk.Frame(window, relief=tk.RIDGE, borderwidth=3, bg="#EB5E28")
f1.grid(row=0, column=1, sticky="nsew")
f1.rowconfigure(0,minsize=60, pad=2, weight=1)
f1.columnconfigure([0,1], minsize=80, pad=2, weight=1)
#APP NAME
"""logoFrame = tk.Frame(f1, relief=tk.GROOVE, pady=10)
logoFrame.grid(row=0, column=1, sticky="nsew")"""
logo = tk.Label(f1, text="Task Manager", bg="#EB5E28", fg="white", font=("Fantasy",50,"italic"))
logo.grid(row=0, column=1, sticky="nsew")
#New task entry section
inputFrame = tk.Frame(f1, relief=tk.GROOVE, pady=10)
inputFrame.grid(row=1, column=0, sticky="nsew")

new_taskLbl = tk.Label(inputFrame, text="Enter a task", fg="#252422", font=("bold"))
new_taskLbl.pack(side=tk.LEFT, padx=10)

newtaskEnt = tk.Entry(inputFrame)
newtaskEnt.pack(side=tk.LEFT, padx=10)

add_Task_Btn = tk.Button(inputFrame, text="Add Task", bg="#CCC5B9", fg="#252422", command=addTask)
add_Task_Btn.pack(side=tk.LEFT, padx=10)

#Additional Frame that contains info
infoFrame =  tk.Frame(f1, relief=tk.GROOVE)
infoFrame.grid(row=1, column=1, sticky="nsew")
information = f"Pending Tasks: \t{info['Pending Tasks']} \nCompleted Tasks: {info['Completed Tasks']}" 
msg = tk.Message(infoFrame, text=information)
msg.pack(side=tk.TOP)
"""
showBtn = tk.Button(infoFrame, text="Show Details", bg="#CCC5B9", fg="#252422", command=show)
showBtn.pack(side=tk.TOP)"""

#FRAME2
#frame to that contains task list
f2 = tk.Frame(window, relief=tk.RIDGE, borderwidth=3, bg="#252422")
f2.grid(row=0,column=0, sticky="nsew")

taskframe = tk.Frame(f2, relief=tk.RIDGE, borderwidth=3)
taskframe.pack(side=tk.TOP, fill="x")
label = tk.Label(taskframe, text="Tasks TO DO", bg="#252422", fg="white", font=("Gill Sans",30,"bold"))
label.pack(side=tk.TOP, fill="x")

window.mainloop()