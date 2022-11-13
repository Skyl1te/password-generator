import random
import tkinter as tk
from tkinter import *

letters = 'qwertyuiopasdfghjklzxcvbnm'
symbols= '!@#$%^&*()*+-'
caps_letters = letters.upper()
password = ''

window = tk.Tk(className='Password generator')
window.resizable(width=False, height=False)
window.geometry('600x350')
window.configure(bg='orange')
show_password = tk.Entry(window, width=50, bg='gray', font='Arial, 20', foreground='white')

def generate():
    global password 
    password = ''
    show_password.delete(0, END)
    for i in range(0, 10):
       password += random.choice(letters)
       password += random.choice(caps_letters)
       password += random.choice(symbols)
    
    return password, show_password.insert(END, f'{password}')