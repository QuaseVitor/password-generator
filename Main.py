from customtkinter import *
import random
import string
import pyperclip



def generate():
    password = ""
    aux = ""
    for x in range(10):
        aux = ''.join(random.choices(string.ascii_uppercase+ string.ascii_lowercase  +
                             string.digits))
        password += aux
        
    print(password)
    text_gen.configure(text=password)
    pyperclip.copy(password)
    return password



window = CTk()
window.title("Password Generate")
window.geometry("720x480")

text_main = CTkLabel(window, text="Gerador de senha", font=("Arial", 50))
text_main.place(anchor='center',
                relx=0.5,
                rely=0.15)

button_gen = CTkButton(window, text="Gerar", width=250, height=50, command=generate)
button_gen.place(anchor='center',
                relx=0.5,
                rely=0.70)

#button_copy = CTkButton(window, text="1", width=50, height=50, command=copy )
#button_copy.place(anchor='center',
                #relx=0.715,
                #rely=0.70)

text_gen = CTkLabel(window, text="", font=('Arial', 60))
text_gen.place(anchor='center',
               relx=0.5,
               rely=0.45)

window.mainloop()