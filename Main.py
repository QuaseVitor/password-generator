from customtkinter import *
import random
import string
import pyperclip

valor = 8
onlynum = 0

def ajuste(value):
    global valor
    valor = int(value)
     

def check():
    global onlynum
    onlynum = only.get()

def generate():
    password = ""
    aux = ""
    
    if onlynum==1:
        for x in range(valor):
            aux = ''.join(random.choices(string.digits))
            password += aux
        
    else:
        for x in range(valor):
            aux = ''.join(random.choices(string.ascii_uppercase+ string.ascii_lowercase  +
                                string.digits))
            password += aux
    
    text_gen.configure(text=password)
    pyperclip.copy(password)
    

def copy():
    pyperclip.copy(text_gen.cget("text"))

window = CTk()
window.title("Password Generate")
window.geometry("720x480")
window.minsize(width=720, height=480)
window.maxsize(width=720, height=480)

text_main = CTkLabel(window, text="Gerador de senha", font=("Arial", 50))
text_main.place(anchor='center',
                relx=0.5,
                rely=0.15)

button_gen = CTkButton(window, text="Gerar", width=250, height=50, command=generate, font=('Arial', 35))
button_gen.place(anchor='center',
                relx=0.475,
                rely=0.70)

button_copy = CTkButton(window, text="1", width=50, height=50, command=copy )
button_copy.place(anchor='center',
                relx=0.6875,
                rely=0.70)

text_gen = CTkLabel(window, text="", font=('Arial', 80))
text_gen.place(anchor='center',
               relx=0.5,
               rely=0.45)


ajust = CTkSlider(window, from_=4, to=10, number_of_steps=3, command=ajuste)
ajust.place(anchor="center", relx=0.5,rely=0.85)

only = CTkCheckBox(window, text="Apenas numeros", command=check)
only.place(anchor="center", relx=0.5,rely=0.925)


window.mainloop()