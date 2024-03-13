from tkinter import *
import articulos

class MerksAndSpenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Merks and Spen")

        self.nombre_var = StringVar()
        self.precio_var = StringVar()
        self.cantidad_var = StringVar()

        
        Label(root, text="Nombre del artículo:").grid(row=0, column=0)
        self.nombre_entry = Entry(root, textvariable=self.nombre_var)
        self.nombre_entry.grid(row=0, column=1)

        Label(root, text="Precio:").grid(row=1, column=0)
        self.precio_entry = Entry(root, textvariable=self.precio_var)
        self.precio_entry.grid(row=1, column=1)

        Label(root, text="Cantidad:").grid(row=2, column=0)
        self.cantidad_entry = Entry(root, textvariable=self.cantidad_var)
        self.cantidad_entry.grid(row=2, column=1)

        Button(root, text="Agregar", command=self.agregar_articulo).grid(row=3, column=0)
        Button(root, text="Eliminar", command=self.eliminar_articulo).grid(row=3, column=1)
        Button(root, text="Modificar", command=self.modificar_articulo).grid(row=3, column=2)

    def agregar_articulo(self):
        nombre = self.nombre_var.get()
        precio = self.precio_var.get()
        cantidad = self.cantidad_var.get()
      

    def eliminar_articulo(self):
        
        pass

    def modificar_articulo(self):
  
        pass

if __name__ == "__main__":
    root = Tk()
    app = MerksAndSpenApp(root)
    root.mainloop()
