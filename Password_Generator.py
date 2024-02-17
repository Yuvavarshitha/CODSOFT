import random
import string
import tkinter as tk
from tkinter import font



def printOP():
    print(lenEntry.get(), checkOpt1.get(), checkOpt2.get(), checkOpt3.get(), checkOpt4.get())

#minimum password length will be 6
def generate_password(length, lowerCase, upperCase, symbol, number):
    length = int(length)
    inc = 1
    pwd = ''
    alphabets = ''
    numerals = ''
    symbols = ''
    #Charcters used in password
    if lowerCase and upperCase:
        alphabets = ''.join(random.choice(string.ascii_letters) for i in range(length-4))
    elif lowerCase:
        alphabets = ''.join(random.choice(string.ascii_lowercase) for i in range(length-4))
    else:
        alphabets = ''.join(random.choice(string.ascii_uppercase) for i in range(length-4))

    #symbols used in the password
    if symbol:
        symbols = ''.join(random.choice(string.punctuation) for i in range(2))
    #numbers used in the password
    if number:
        numerals = ''.join(random.choice(string.digits) for i in range(2))

    pwd = alphabets + symbols + numerals

    showResult(pwd)

def showResult(password):
    msg = tk.Message(frame1, text=password)
    msg.pack(side=tk.TOP)

#print ( "Genrated Password: ", generate_password(10, True, True, True, True))

window = tk.Tk()
window.configure(background="#EB5E28")
window.geometry("500x500")

label = tk.Label(window, text="PassWord Generator", bg = "#EB5E28", font=("Arial", 20))
label.pack(side=tk.TOP)

frame1 = tk.Frame(window)
frame1.pack(side=tk.TOP)

inpLabel = tk.Label(frame1, text="Specify Password length", font=("Arial", 20))
inpLabel.pack(side=tk.TOP)

lenEntry = tk.Entry(frame1)
lenEntry.pack(side=tk.TOP)

incLabel = tk.Label(frame1, text="Password should include: ", font=("Arial", 20))
incLabel.pack(side=tk.TOP)

checkOpt1 = tk.BooleanVar()
checkOpt2 = tk.BooleanVar()
checkOpt3 = tk.BooleanVar()
checkOpt4 = tk.BooleanVar()

opt1 = tk.Checkbutton(frame1, text="Lowercase", variable=checkOpt1, onvalue=True, offvalue=False, font=("Helvetica", 20))
opt1.pack(side=tk.TOP)

opt2 = tk.Checkbutton(frame1, text="Uppercase", variable=checkOpt2, onvalue=True, offvalue=False, font=("Helvetica", 20))
opt2.pack(side=tk.TOP)

opt3 = tk.Checkbutton(frame1, text="Symbols", variable=checkOpt3, onvalue=True, offvalue=False, font=("Arial", 20))
opt3.pack(side=tk.TOP)

opt4 = tk.Checkbutton(frame1, text="Numbers", variable=checkOpt4, onvalue=True, offvalue=False, font=("Arial", 20))
opt4.pack(side=tk.TOP)

#lambda: generate_password(lenEntry.get(), checkOpt1, checkOpt2, checkOpt3, checkOpt4)
genBtn = tk.Button(frame1, text="Generate Password", 
                   command=lambda: generate_password(lenEntry.get(), checkOpt1.get(), checkOpt2.get(), checkOpt3.get(), checkOpt4.get()), 
                   font=("Arial", 20),
                   bg = "#CCC5B9")
genBtn.pack(side=tk.TOP)

msg = tk.Message(frame1, text="")
msg.pack(side=tk.TOP)

window.mainloop()
