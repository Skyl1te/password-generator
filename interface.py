from function import *

tk.Label(window, text="Your Password", font='Arial, 30', bg='orange', foreground='white').place(x=165, y=20)
tk.Button(window, width=20, text='Generate', font='Arial, 20', bg='red', command=generate, foreground='white').place(x=135, y=200)
tk.Label(window, text="Password Generator", font='Arial, 30', bg='orange', foreground='white').place(x=600//5, y=290)

show_password.pack(pady=130)

window.mainloop()