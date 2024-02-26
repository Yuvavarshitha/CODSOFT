import random
import string
import tkinter as tk
from tkinter import font

#minimum password length will be 6
def generate_password(length, lowerCase, upperCase, symbol, number):
    length = int(length)
    char_to_use = ''
    #Charcters used in password
    if lowerCase and upperCase:
        char_to_use+=(string.ascii_letters)
    elif lowerCase:
        char_to_use+=(string.ascii_lowercase)
    elif upperCase:
        char_to_use+=(string.ascii_uppercase)

    #symbols used in the password
    if symbol:
        char_to_use+=string.punctuation
    #numbers used in the password
    if number:
        char_to_use+=(string.digits)

    pwd = ''.join(random.choice(char_to_use) for i in range(length))

    showResult(pwd)

def showResult(password):
    pwdField.delete(0,tk.END)
    pwdField.insert(0,password)

window = tk.Tk()
window.configure(background="#3C3633")
window.geometry("500x500")

label = tk.Label(window, text="PassWord Generator", fg="#E0CCBE",bg = "#3C3633", font=("Fantasy",30,"italic"))
label.pack(side=tk.TOP, pady=30)

frame1 = tk.Frame(window)
frame1.pack(side=tk.TOP, padx=20)

inpLabel = tk.Label(frame1, text="Specify Password length", font=("Arial", 17))
inpLabel.pack(side=tk.TOP,padx=20, pady=10)

lenEntry = tk.Entry(frame1)
lenEntry.pack(side=tk.TOP,padx=20)

incLabel = tk.Label(frame1, text="Password should include: ", font=("Arial", 17))
incLabel.pack(side=tk.TOP,padx=20,pady=10)

checkOpt1 = tk.BooleanVar()
checkOpt2 = tk.BooleanVar()
checkOpt3 = tk.BooleanVar()
checkOpt4 = tk.BooleanVar()

opt1 = tk.Checkbutton(frame1, text="Lowercase", variable=checkOpt1, onvalue=True, offvalue=False, font=("Helvetica", 17))
opt1.pack(side=tk.TOP,padx=20, anchor="w")

opt2 = tk.Checkbutton(frame1, text="Uppercase", variable=checkOpt2, onvalue=True, offvalue=False, font=("Helvetica", 17))
opt2.pack(side=tk.TOP,padx=20, anchor="w")

opt3 = tk.Checkbutton(frame1, text="Symbols", variable=checkOpt3, onvalue=True, offvalue=False, font=("Arial", 17))
opt3.pack(side=tk.TOP,padx=20, anchor="w")

opt4 = tk.Checkbutton(frame1, text="Numbers", variable=checkOpt4, onvalue=True, offvalue=False, font=("Arial", 17))
opt4.pack(side=tk.TOP,padx=20, anchor="w")

#lambda: generate_password(lenEntry.get(), checkOpt1, checkOpt2, checkOpt3, checkOpt4)
genBtn = tk.Button(frame1, text="Generate Password", 
                   command=lambda: generate_password(lenEntry.get(), checkOpt1.get(), checkOpt2.get(), checkOpt3.get(), checkOpt4.get()), 
                   font=("Arial", 15),
                   bg = "#CCC5B9")
genBtn.pack(side=tk.TOP,padx=20)

pwdField = tk.Entry(frame1)
pwdField.pack(side=tk.TOP,padx=20, pady=10)

window.mainloop()
