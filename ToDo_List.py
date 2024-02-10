import tkinter as tk

#Show no of completed task
#show no of pending task

taskList = ["Wake Up", "Brush Teeth"]
completedTasks = []
info = {"Pending Tasks":len(taskList),"Completed Tasks":len(completedTasks) }
def show():
    for i, j in info.items():
        new_infoFrame = tk.Frame(infoFrame)
        new_infoFrame.pack(side=tk.TOP)
        lbl = tk.Label(new_infoFrame, text=i)
        lbl.pack()
        lblval = tk.Label(new_infoFrame,text=j)
        lblval.pack()

def addTask():
    #function that executes when the current task is completed 
    def comTask():
        comlabel = tk.Label(f1, text="task")
        #comlabel.pack(tk.BOTTOM, fill)
        taskList.remove(task)
        completedTasks.append(task)
        taskframe.destroy()

    task = newtaskEnt.get()
    taskList.append(task)
    newtaskEnt.delete(0,tk.END)

    taskframe = tk.Frame(f2, relief=tk.RIDGE, borderwidth=3, width=100)
    taskframe.pack(side=tk.TOP, fill="x") #fill='x' is used to utilize the entire available width left after allocating space for the widgets

    new_task = tk.Label(taskframe, text=task, bg="black", fg="white",)
    new_task.pack(side=tk.LEFT, fill="x")

    del_btn = tk.Button(taskframe, text="Delete", bg="red", fg="black", command=taskframe.destroy)
    del_btn.pack(side=tk.RIGHT)
    com_btn = tk.Button(taskframe, text="Complete", bg="green", fg="black", command=comTask)
    com_btn.pack(side=tk.RIGHT)



window = tk.Tk()

#Organize the frames inside the window using the grid geometry manager
#the window will have Two Frames
window.rowconfigure(0, minsize=200, pad=2, weight=1)
window.columnconfigure([0,1], minsize=300, pad=2, weight=1)

#FRAME1
#frame that inputs a new task and adds it to task list and displays details
f1 = tk.Frame(window, relief=tk.RIDGE, borderwidth=3, )
f1.grid(row=0, column=1, sticky="nsew")
#APP NAME
logo = tk.Label(f1, text="Task Manager", bg="black", fg="white", font=("Fantasy",20,"bold"))
logo.pack(side=tk.TOP, pady=5)
#New task entry section
inputFrame = tk.Frame(f1, relief=tk.GROOVE)
inputFrame.pack(side=tk.TOP, fill="x")
new_taskLbl = tk.Label(inputFrame, text="Enter a task", bg="black", fg="white")
new_taskLbl.pack(side=tk.LEFT)
newtaskEnt = tk.Entry(inputFrame)
newtaskEnt.pack(side=tk.LEFT)
add_Task_Btn = tk.Button(inputFrame, text="Add Task", bg="black", fg="white", command=addTask)
add_Task_Btn.pack(side=tk.LEFT)

#Additional Frame that contains info
infoFrame =  tk.Frame(f1, relief=tk.GROOVE)
infoFrame.pack(side=tk.TOP, fill="both")

showBtn = tk.Button(infoFrame, text="Show Details", bg="black", fg="white", command=show)
showBtn.pack(side=tk.LEFT)

#FRAME2
#frame to that contains task list
f2 = tk.Frame(window, relief=tk.RIDGE, borderwidth=3)
f2.grid(row=0,column=0, sticky="nsew")
label = tk.Label(f2, text="Tasks TO DO", bg="black", fg="white")
label.pack(side=tk.TOP)

taskframe = tk.Frame(f2, relief=tk.RIDGE, borderwidth=3)
taskframe.pack(side=tk.TOP, fill="x")
label = tk.Label(taskframe, text="Wake UP", bg="black", fg="white")
label.pack(side=tk.TOP, fill="x")

window.mainloop()