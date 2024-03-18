from tkinter import Tk, Entry, Label, Button, Checkbutton, BooleanVar, messagebox

def toggle_password_visibility():
    if password_visible.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

def show_password():
    messagebox.showinfo("Contraseña", f"Contraseña ingresada: {entry_password.get()}")

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "usuario" and password == "contraseña":
        messagebox.showinfo("Login exitoso", "Inicio de sesión exitoso!")
    else:
        messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")

# Crear la ventana principal
root = Tk()
root.title("Inicio de sesión")
root.geometry("350x200")  # Ajuste de la geometría de la ventana

# Crear los widgets
label_username = Label(root, text="Departamento:")
label_username.grid(row=0, column=0, padx=5, pady=5)

entry_username = Entry(root)
entry_username.grid(row=0, column=1, padx=5, pady=5)

label_password = Label(root, text="Contraseña:")
label_password.grid(row=1, column=0, padx=5, pady=5)

entry_password = Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

password_visible = BooleanVar()
check_button_show_password = Checkbutton(root, text="Mostrar contraseña", variable=password_visible, command=toggle_password_visibility)
check_button_show_password.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

button_login = Button(root, text="Iniciar sesión", command=login)
button_login.grid(row=3, column=0, padx=5, pady=5)

button_show_password = Button(root, text="Ver contraseña", command=show_password)
button_show_password.grid(row=3, column=1, padx=5, pady=5)

# Iniciar el bucle principal
root.mainloop()
