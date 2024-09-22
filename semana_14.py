# Semana 14
# Tarea: Creación de una Aplicación de Agenda Personal

import tkinter as tk
from tkinter import ttk, messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Agenda Personal")

# Lista para manejar los eventos como diccionarios
eventos = []

# Frame para la lista de eventos
frame_lista = ttk.Frame(ventana)
frame_lista.pack(side="top", fill="both", expand=True)

# Treeview para mostrar los eventos
columnas = ("fecha", "hora", "descripcion")
tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")
tree.heading("fecha", text="Fecha")
tree.heading("hora", text="Hora")
tree.heading("descripcion", text="Descripción")
tree.pack(side="left", fill="both", expand=True)

# Scrollbar para la lista de eventos
scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

# Frame para los campos de entrada y botones
frame_entradas = ttk.Frame(ventana)
frame_entradas.pack(side="bottom")

# Campos de entrada
etiqueta_fecha = ttk.Label(frame_entradas, text="Fecha:")
etiqueta_fecha.grid(row=0, column=0)
entrada_fecha = ttk.Entry(frame_entradas)
entrada_fecha.grid(row=0, column=1)

etiqueta_hora = ttk.Label(frame_entradas, text="Hora:")
etiqueta_hora.grid(row=1, column=0)
entrada_hora = ttk.Entry(frame_entradas)
entrada_hora.grid(row=1, column=1)

etiqueta_descripcion = ttk.Label(frame_entradas, text="Descripción:")
etiqueta_descripcion.grid(row=2, column=0)
entrada_descripcion = ttk.Entry(frame_entradas)
entrada_descripcion.grid(row=2, column=1)

# Botones
boton_agregar = ttk.Button(frame_entradas, text="Agregar Evento")
boton_agregar.grid(row=3, column=0)

boton_eliminar = ttk.Button(frame_entradas, text="Eliminar Evento")
boton_eliminar.grid(row=3, column=1)

boton_salir = ttk.Button(frame_entradas, text="Salir", command=ventana.quit)
boton_salir.grid(row=3, column=2)


# Función para agregar un evento a la lista
def agregar_evento():
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    # Agregar a la lista de eventos y al Treeview
    evento = {"fecha": fecha, "hora": hora, "descripcion": descripcion}
    eventos.append(evento)
    tree.insert("", "end", values=(fecha, hora, descripcion))

    entrada_fecha.delete(0, tk.END)
    entrada_hora.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)


# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar el evento?"):
            # Eliminar de la lista de eventos
            for i, evento in enumerate(eventos):
                if (evento["fecha"], evento["hora"], evento["descripcion"]) == tree.item(seleccionado, "values"):
                    del eventos[i]
                    break
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("Advertencia", "No hay ningún evento seleccionado")


# Asociar las funciones a los botones
boton_agregar.config(command=agregar_evento)
boton_eliminar.config(command=eliminar_evento)

# Iniciar la aplicación
ventana.mainloop()

# Universidad Estatal Amazónica
# Andrés Ponce M.