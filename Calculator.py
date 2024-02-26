import tkinter as tk
import string

expression = ""

def perform(btn):
    global expression #change a global variable inside the function
    if btn == '=':
        ans = int(eval(expression))
        expression = str(ans)
        expInput.delete(0, tk.END)
        expInput.insert(tk.END, ans)
        
    else:
        if btn == 'x':
            expInput.insert(tk.END, 'x')
            expression += '*'
        else:
            expInput.insert(tk.END, btn)
            expression += str(btn)


window = tk.Tk()
#window.geometry("500x500")

window.rowconfigure([0,1,2,3,4], weight=1)
window.columnconfigure([0,1,2,3], weight=1)

expInput = tk.Entry(window)
expInput.grid(row=0, column=0, columnspan=4, sticky="ew")


btndot = tk.Button(text='.', width=10, height=2, command=lambda: perform('.'))
btndot.grid(row=4, column=0, sticky="nsew")

btn0 = tk.Button(text='0', width=10, height=2, command=lambda: perform(0))
btn0.grid(row=4, column=1, sticky="nsew")

btneq = tk.Button(text='=', width=10, height=2, command=lambda: perform('='))
btneq.grid(row=4, column=2, sticky="nsew")

btnplus = tk.Button(text='+', width=10, height=2, command=lambda: perform('+'))
btnplus.grid(row=4, column=3, sticky="nsew")

btn1 = tk.Button(text='1', width=10, height=2, command=lambda: perform(1))
btn1.grid(row=3, column=0, sticky="nsew")

btn2 = tk.Button(text='2', width=10, height=2, command=lambda: perform(2))
btn2.grid(row=3, column=1, sticky="nsew")

btn3 = tk.Button(text='3', width=10, height=2, command=lambda: perform(3))
btn3.grid(row=3, column=2, sticky="nsew")

btnminus = tk.Button(text='-', width=10, height=2, command=lambda: perform('-'))
btnminus.grid(row=3, column=3, sticky="nsew")

btn4 = tk.Button(text='4', width=10, height=2, command=lambda: perform(4))
btn4.grid(row=2, column=0, sticky="nsew")

btn5 = tk.Button(text='5', width=10, height=2, command=lambda: perform(5))
btn5.grid(row=2, column=1, sticky="nsew")

btn6 = tk.Button(text='6', width=10, height=2, command=lambda: perform(6))
btn6.grid(row=2, column=2, sticky="nsew")

btnmul = tk.Button(text='x', width=10, height=2, command=lambda: perform('x'))
btnmul.grid(row=2, column=3, sticky="nsew")


btn7 = tk.Button(text='7', width=10, height=2, command=lambda: perform(7))
btn7.grid(row=1, column=0, sticky="nsew")

btn8 = tk.Button(text='8', width=10, height=2, command=lambda: perform(8))
btn8.grid(row=1, column=1, sticky="nsew")

btn9 = tk.Button(text='9', width=10, height=2, command=lambda: perform(9))
btn9.grid(row=1, column=2, sticky="nsew")

btndiv = tk.Button(text='/', width=10, height=2, command=lambda: perform('/'))
btndiv.grid(row=1, column=3, sticky="nsew")


window.mainloop()