from tkinter import Tk, Frame, Label, Entry, Button, messagebox

# Función para verificar las credenciales
def login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
    elif username == "nombre_del_departamento" and password == "contraseña":
        messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
    else:
        messagebox.showerror("Error", "Credenciales incorrectas.")

# Creamos la ventana
ventana = Tk()
ventana.title("Módulo de Login")
ventana.geometry("400x200")

# Creamos frame
seccion = Frame(ventana)
seccion.pack(pady=20)

# Agregamos etiquetas y campos de entrada
username_label = Label(seccion, text="Nombre del departamento:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = Entry(seccion, width=30)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = Label(seccion, text="Contraseña:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = Entry(seccion, show="*", width=30)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Agregamos botón de login
login_button = Button(seccion, text="Iniciar Sesión", command=login)
login_button.grid(row=2, columnspan=2, pady=10)

# Ejecutamos la ventana
ventana.mainloop()
