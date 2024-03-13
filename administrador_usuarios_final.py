import tkinter
from tkinter import messagebox

# Lista de ejemplo para manejar usuarios en memoria con roles, contraseñas y departamentos
usuarios = {'admin': {'password': 'adminpass', 'role': 'administrador', 'department': 'admin department'}}

# Agregar un nuevo usuario
def agregar_usuario():
    username = entrada_usuario.get()
    password = entrada_contraseña.get()
    department = entrada_departamento.get()
    admin_password = entrada_contraseña_admin.get()
    
    # Verificar la contraseña de administrador antes de agregar un usuario
    if es_admin(admin_password):
        if username in usuarios:
            messagebox.showerror("Error", "El usuario ya existe.")
        else:
            usuarios[username] = {'password': password, 'role': 'usuario', 'department': department}
            actualizar_lista_usuarios()
    else:
        messagebox.showerror("Error", "Contraseña de administrador incorrecta.")

# Eliminar un usuario existente
def eliminar_usuario():
    username = entrada_usuario.get()
    admin_password = entrada_contraseña_admin.get()
    if es_admin(admin_password):
        if username in usuarios and username != 'admin':  # Evitar que se elimine el admin
            del usuarios[username]
            actualizar_lista_usuarios()
        else:
            messagebox.showerror("Error", "El usuario no existe o no se puede eliminar.")
    else:
        messagebox.showerror("Error", "Contraseña de administrador incorrecta.")

# Modificar un usuario existente
def modificar_usuario():
    username = entrada_usuario.get()
    password = entrada_contraseña.get()
    department = entrada_departamento.get()
    admin_password = entrada_contraseña_admin.get()
    if es_admin(admin_password):
        if username in usuarios:
            usuarios[username]['password'] = password
            usuarios[username]['department'] = department
            actualizar_lista_usuarios()
        else:
            messagebox.showerror("Error", "El usuario no existe.")
    else:
        messagebox.showerror("Error", "Contraseña de administrador incorrecta.")

# Verificar si la contraseña proporcionada es la del admin
def es_admin(password):
    return usuarios.get('admin')['password'] == password

# Actualizar la lista de usuarios en la interfaz
def actualizar_lista_usuarios():
    lista_usuarios.delete(0, tkinter.END)
    for usuario, info in usuarios.items():
        lista_usuarios.insert(tkinter.END, f"{usuario} - {info['role']} - {info['department']}")

# Crear la ventana principal
root = tkinter.Tk()
root.title("Sistema de Control de Usuarios")
root.geometry("500x300")  # Ajuste de la geometría de la ventana

# Crear los frames para la organización de los widgets
frame_arriba = tkinter.Frame(root)
frame_arriba.pack()

frame_medio = tkinter.Frame(root)
frame_medio.pack()

frame_abajo = tkinter.Frame(root)
frame_abajo.pack()

# Crear y organizar los widgets en el frame superior
label_usuario = tkinter.Label(frame_arriba, text="Usuario:")
label_usuario.grid(row=0, column=0)

entrada_usuario = tkinter.Entry(frame_arriba)
entrada_usuario.grid(row=0, column=1)

label_contraseña = tkinter.Label(frame_arriba, text="Contraseña:")
label_contraseña.grid(row=1, column=0)

entrada_contraseña = tkinter.Entry(frame_arriba, show="*")
entrada_contraseña.grid(row=1, column=1)

label_departamento = tkinter.Label(frame_arriba, text="Departamento:")
label_departamento.grid(row=2, column=0)

entrada_departamento = tkinter.Entry(frame_arriba)
entrada_departamento.grid(row=2, column=1)

label_contraseña_admin = tkinter.Label(frame_arriba, text="Contraseña Admin:")
label_contraseña_admin.grid(row=3, column=0)

entrada_contraseña_admin = tkinter.Entry(frame_arriba, show="*")
entrada_contraseña_admin.grid(row=3, column=1)

# Crear y organizar los botones para agregar, eliminar y modificar usuarios
boton_agregar = tkinter.Button(frame_medio, text="Agregar Usuario", command=agregar_usuario)
boton_agregar.grid(row=0, column=0)

boton_eliminar = tkinter.Button(frame_medio, text="Eliminar Usuario", command=eliminar_usuario)
boton_eliminar.grid(row=0, column=1)

boton_modificar = tkinter.Button(frame_medio, text="Modificar Usuario", command=modificar_usuario)
boton_modificar.grid(row=0, column=2)

# Crear la lista de usuarios en el frame inferior
lista_usuarios = tkinter.Listbox(frame_abajo)
lista_usuarios.pack()

# Inicializar la lista de usuarios
actualizar_lista_usuarios()

# Ejecutar el bucle principal
root.mainloop()
