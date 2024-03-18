from tkinter import Tk, Frame, Label, Entry, Button, Listbox, messagebox, simpledialog
from tkinter import ttk

class OfficeSupplyRequestApp:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Sistema de Solicitudes de Artículos de Oficina")
        self.ventana.geometry("600x400")
        
        self.tabControl = ttk.Notebook(self.ventana)
        
        self.create_request_tab = CreateRequestTab(self.tabControl)
        self.view_requests_tab = ViewRequestsTab(self.tabControl)
        
        self.tabControl.add(self.create_request_tab, text="Crear Solicitud")
        self.tabControl.pack(expand=1, fill="both")
        
        self.admin_logged_in = False
        self.admin_button = Button(self.ventana, text="Iniciar sesión como administrador", command=self.admin_login)
        self.admin_button.pack()
        
        self.ventana.mainloop()
        
    def admin_login(self):
        password = simpledialog.askstring("Login", "Ingrese la contraseña de administrador:")
        if password == "admin123":
            self.admin_logged_in = True
            self.tabControl.add(self.view_requests_tab, text="Ver Solicitudes")
            self.admin_button.pack_forget()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta. Acceso denegado.")

class CreateRequestTab(Frame):
    def __init__(self, parent):
        self.parent = parent    
        Frame.__init__(self, parent)
        self.department_label = Label(self, text="Departamento:")
        self.department_entry = Entry(self)
        
        self.item_label = Label(self, text="Artículo:")
        self.item_entry = Entry(self)
        
        self.quantity_label = Label(self, text="Cantidad:")
        self.quantity_entry = Entry(self)
        
        self.create_button = Button(self, text="Crear Pedido", command=self.create_request)
        
        self.department_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.department_entry.grid(row=0, column=1, padx=10, pady=10)
        self.item_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.item_entry.grid(row=1, column=1, padx=10, pady=10)
        self.quantity_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=10)
        self.create_button.grid(row=3, columnspan=2, pady=10)
        
    def create_request(self):
        messagebox.showinfo("Información", "Pedido creado exitosamente.")
        
class ViewRequestsTab(Frame):
    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self, parent)
        self.requests_listbox = Listbox(self)
        self.requests_listbox.pack(expand=True, fill="both")
        
        self.refresh_button = Button(self, text="Actualizar", command=self.refresh_requests)
        self.refresh_button.pack()
        
    def refresh_requests(self):
        messagebox.showinfo("Información", "Lista de solicitudes actualizada.")

OfficeSupplyRequestApp().ventana.mainloop()
