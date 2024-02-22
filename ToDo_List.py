import tkinter as tk
from tkinter import *
#Show no of completed task
#show no of pending task

taskList = dict()
completedTasks = []
info = {"Pending Tasks":len(taskList.keys()),
        "Completed Tasks":len(completedTasks),
        "High": list(taskList.values()).count('High'),
        "Medium": list(taskList.values()).count('Medium'),
        "Normal": list(taskList.values()).count('Normal')
        }

def update():
    info["Pending Tasks"] = len(list(taskList.keys()))
    info["Completed Tasks"] = len(completedTasks)
    info['High'] = list(taskList.values()).count('High')
    info['Medium'] = list(taskList.values()).count('Medium')
    info['Normal'] = list(taskList.values()).count('Normal')
    msg1.configure(text= f"\n\nPending Tasks:   {info['Pending Tasks']} \nCompleted Tasks:   {info['Completed Tasks']}")
    msg2.configure(text=f"\nHigh Priority: {info['High']} \n\nMedium Priority: {info['Medium']} \n\nNormal Priority: {info['Normal']}")
    print(taskList, info)

def addTask():
    #function that executes when the current task is completed 
    def comTask():
        taskList.pop(task)
        info["Pending Tasks"] = len(list(taskList.keys()))
        completedTasks.append(task)
        info["Completed Tasks"] = len(completedTasks)
        taskframe.destroy()
        update()
    #function that executes when the current task is deleted
    def delTask():
        taskList.pop(task)
        info["Pending Tasks"] = len(taskList.keys())
        taskframe.destroy()
        update()

    task = newtaskEnt.get()
    task_priority = priority.get().strip()
    taskList[task] = task_priority
    newtaskEnt.delete(0,tk.END)
    
    #Creating a frame for the new task
    
    taskframe = tk.Frame(tasks, relief=tk.RIDGE, borderwidth=3, width=100, bg="#252422")

    new_task = tk.Label(taskframe, text=task, fg="white", bg="#252422", font=("bold"))
    new_task.pack(side=tk.LEFT, fill="x")

    del_btn = tk.Button(taskframe, text="Delete", bg="red", fg="black", command=delTask)
    del_btn.pack(side=tk.RIGHT)
    com_btn = tk.Button(taskframe, text="Complete", bg="green", fg="black", command=comTask)
    com_btn.pack(side=tk.RIGHT)

    if task_priority == "High":
        taskframe.pack(side=tk.TOP, fill="x")
    else:
        taskframe.pack(side=tk.BOTTOM, fill="x") #fill='x' is used to utilize the entire available width left after allocating space for the widgets

    update()

window = tk.Tk()
window.geometry("800x400")
#Organize the frames inside the window using the grid geometry manager
#the window will have Two Frames
window.rowconfigure(0, minsize=200, pad=2, weight=1)
window.columnconfigure([0,1], minsize=300, pad=2, weight=1)

#FRAME1
#frame that inputs a new task and adds it to task list and displays details
f1 = tk.Frame(window, relief=tk.RIDGE, borderwidth=3, bg="#EB5E28")
f1.grid(row=0, column=1, sticky="nsew")

#APP NAME
logoFrame = tk.Frame(f1, relief=tk.GROOVE, pady=10, bg="#EB5E28")
logoFrame.pack(side=tk.TOP, fill="both")
logo = tk.Label(logoFrame, text="Task Manager", bg="#EB5E28", fg="white", font=("Fantasy",40,"italic"))
logo.pack()
#New task entry section
inputFrame = tk.Frame(f1, relief=tk.GROOVE, pady=10)
inputFrame.pack(side=tk.TOP, fill="both")

new_taskLbl = tk.Label(inputFrame, text="Enter a task", fg="#252422", font=("bold"))
new_taskLbl.pack(side=tk.LEFT, padx=10)

newtaskEnt = tk.Entry(inputFrame)
newtaskEnt.pack(side=tk.LEFT, padx=10)

#Adding Priority to each task
inputFrame2 = tk.Frame(f1, relief=tk.GROOVE, pady=10)
inputFrame2.pack(side=tk.TOP, fill="both")

priority = StringVar()
priority.set("Normal ")
options = ["Normal ", "Medium", "  High  "]
priorityLabel = tk.Label(inputFrame2, text="Select Priority", fg="#252422", font=("bold"))
priorityLabel.pack(side=tk.LEFT, padx=10)

priorityInp = OptionMenu(inputFrame2, priority, *options)
priorityInp.pack(side=tk.LEFT, padx=10)

#Add Task Button
add_Task_Btn = tk.Button(inputFrame2, text="Add Task", bg="#CCC5B9", fg="#252422", command=addTask)
add_Task_Btn.pack(side=tk.LEFT, padx=20)


#Additional Frame that contains info
infoFrame =  tk.Frame(f1, relief=tk.GROOVE)
infoFrame.pack(side=tk.TOP, fill="both")
information = f"\n\nPending Tasks:   {info['Pending Tasks']} \n\nCompleted Tasks:   {info['Completed Tasks']}" 
infos = f"\nHigh Priority: {info['High']} \n\nMedium Priority: {info['Medium']} \n\nNormal Priority: {info['Normal']}"
msg1 = tk.Message(infoFrame, text=information, width=150)
msg1.pack(side=tk.LEFT, padx=50)
msg2 = tk.Message(infoFrame, text=infos, width=150)
msg2.pack(side=tk.RIGHT, padx=50)


#FRAME2
#frame to that contains task list
f2 = tk.Frame(window, relief=tk.RIDGE, borderwidth=3, bg="#252422")
f2.grid(row=0,column=0, sticky="nsew")

taskframe = tk.Frame(f2, relief=tk.RIDGE, borderwidth=3)
taskframe.pack(side=tk.TOP, fill="x")
label = tk.Label(taskframe, text="Tasks TO DO", bg="#252422", fg="white", font=("Gill Sans",30,"bold"))
label.pack(side=tk.TOP, fill="x")

tasks = tk.Frame(taskframe)
tasks.pack(side=tk.TOP, fill="x")

window.mainloop()