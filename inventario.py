from tkinter import *
from tkinter import ttk

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario de Tienda")

        self.tabla = ttk.Treeview(root)
        self.tabla["columns"] = ("nombre", "cantidad", "ubicacion", "reporte")
        self.tabla.heading("nombre", text="Nombre del Artículo")
        self.tabla.heading("cantidad", text="Cantidad Disponible")
        self.tabla.heading("ubicacion", text="Ubicación del Almacén")
        self.tabla.heading("reporte", text="Reporte del Inventario")
        self.tabla.pack(expand=True, fill="both")

        
        self.nombre_label = Label(root, text="Nombre del artículo:")
        self.nombre_label.pack()
        self.nombre_entry = Entry(root)
        self.nombre_entry.pack()

        self.cantidad_label = Label(root, text="Cantidad disponible:")
        self.cantidad_label.pack()
        self.cantidad_entry = Entry(root)
        self.cantidad_entry.pack()

        self.ubicacion_label = Label(root, text="Ubicación del almacén:")
        self.ubicacion_label.pack()
        self.ubicacion_entry = Entry(root)
        self.ubicacion_entry.pack()

        self.reporte_label = Label(root, text="Reporte del inventario:")
        self.reporte_label.pack()
        self.reporte_entry = Entry(root)
        self.reporte_entry.pack()


        self.reporte_button = Button(root, text="Reporte por Departamento", command=self.reporte_departamento)
        self.reporte_button.pack()
        self.reporte_fecha_button = Button(root, text="Reporte por Fechas", command=self.reporte_fechas)
        self.reporte_fecha_button.pack()

 
        self.grafica_button = Button(root, text="Generar Gráfico de Barras", command=self.generar_grafico)
        self.grafica_button.pack()

    def reporte_departamento(self):

        pass

    def reporte_fechas(self):
        
        pass

    def generar_grafico(self):
       
        pass

if __name__ == "__main__":
    root = Tk()
    app = InventarioApp(root)
    root.mainloop()



