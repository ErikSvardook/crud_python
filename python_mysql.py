import tkinter as tk
#Importar los modulos restantes de tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from clientes import *
from connection import *

class FormularioClientes:
    global win
    win = None
    global groupBox
    groupBox = None
    global texBoxId
    texBoxId = None
    global texBoxNombres
    textBoxNombre = None
    global texBoxApellidos
    textBoxApellidos = None
    global combo
    combo = None
    global tree
    tree = None

def actualizarTreeview():
    global tree
    try:
        #Borrar datos actuales del treeview
        tree.delete(*tree.get_children())

        #Obtener los nuevos datos que queremos mostrar
        datos = CClientes.mostrarClientes()

        #Insertar los datos en el treeview
        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)

    except ValueError as error:
        print("Error al actualizar la tabla {}".format(error))


def guardarRegistros():
    global texBoxNombres, texBoxApellidos, combo, groupBox

    try:
        #verificar si los widgets estan inicializados
        if texBoxNombres is None or texBoxApellidos is None or combo is None:
            print("Los widgets no estan inicializados")
            return
        
        nombres = texBoxNombres.get()
        apellidos = texBoxApellidos.get()
        sexo = combo.get()
        CClientes.ingresarClientes(nombres, apellidos, sexo)
        messagebox.showinfo("Información", "Los datos se ingresaron correctamente")

        #Llamamos a la función de actualizar treeview
        actualizarTreeview()

        #Limpiamos las textBox
        texBoxNombres.delete(0, END)
        texBoxApellidos.delete(0, END)

    except ValueError as error:
        print("Error al guardar los datos: {}".format(error))

def modificarRegistros():
    global texBoxId, texBoxNombres, texBoxApellidos, combo, groupBox

    try:
        #verificar si los widgets estan inicializados
        if texBoxId is None or texBoxNombres is None or texBoxApellidos is None or combo is None:
            print("Los widgets no estan inicializados")
            return
        
        idUsuario = texBoxId.get()
        nombres = texBoxNombres.get()
        apellidos = texBoxApellidos.get()
        sexo = combo.get()
        CClientes.modificarClientes(idUsuario, nombres, apellidos, sexo)
        messagebox.showinfo("Información", "Los datos se actualizaron correctamente")

        #Llamamos a la función de actualizar treeview
        actualizarTreeview()

        #Limpiamos las textBox
        texBoxId.delete(0, END)
        texBoxNombres.delete(0, END)
        texBoxApellidos.delete(0, END)

    except ValueError as error:
        print("Error al modificar los datos: {}".format(error))

def eliminarRegistros():
    global texBoxId, texBoxNombres, texBoxApellidos

    try:
        #verificar si los widgets estan inicializados
        if texBoxId is None:
            print("Los widgets no estan inicializados")
            return
        
        idUsuario = texBoxId.get()

        CClientes.eliminarClientes(idUsuario)
        messagebox.showinfo("Información", "Los datos se eliminaron correctamente")

        #Llamamos a la función de actualizar treeview
        actualizarTreeview()

        #Limpiamos las textBox
        texBoxId.delete(0, END)
        texBoxNombres.delete(0, END)
        texBoxApellidos.delete(0, END)

    except ValueError as error:
        print("Error al eliminar los datos: {}".format(error))

def seleccionarRegistro(event):
    try:
        itemSeleccionado = tree.focus()

        if itemSeleccionado:
            #Obtener los valores por columnas
            values = tree.item(itemSeleccionado)["values"]
            
            #Establecer los valores de los widgets Entry
            texBoxId.delete(0, END)
            texBoxId.insert(0, values[0])
            texBoxNombres.delete(0, END)
            texBoxNombres.insert(0, values[1])
            texBoxApellidos.delete(0, END)
            texBoxApellidos.insert(0, values[2])
            combo.set(value[3])


    except ValueError as error:
        print("Error al seleccionar los datos {}".format(error))

def formulario():
    global win
    global groupBox
    global texBoxId
    global texBoxNombres
    global texBoxApellidos
    global combo
    global tree

    try:
        win = Tk()
        win.geometry("1250x300")
        win.title("Formulario de python")
        
        groupBox = LabelFrame(win, text="Datos del personal", padx=5, pady=5)
        groupBox.grid(row=0,column=0,padx=10,pady=10)

        #Elementos del gruopBox de la izquierda
        labelId = Label(groupBox, text="Id", width=13,font=("arial,12")).grid(row=0,column=0)
        texBoxId = Entry(groupBox)
        texBoxId.grid(row=0, column=1)

        labelNombres = Label(groupBox, text="Nombres", width=13,font=("arial,12")).grid(row=1,column=0)
        texBoxNombres = Entry(groupBox)
        texBoxNombres.grid(row=1, column=1)

        labelApellidos = Label(groupBox, text="Apellidos", width=13,font=("arial,12")).grid(row=2,column=0)
        texBoxApellidos = Entry(groupBox)
        texBoxApellidos.grid(row=2, column=1)

        labelSexo = Label(groupBox, text="Sexo", width=13,font=("arial,12")).grid(row=3,column=0)
        seleccionSexo = tk.StringVar()
        combo = ttk.Combobox(groupBox,values=["Masculino","Femenino"], textvariable=seleccionSexo)
        combo.grid(row=3,column=1)
        seleccionSexo.set("Masculino")

        Button(groupBox,text="Guardar", width=10, command=guardarRegistros).grid(row=4,column=0)
        Button(groupBox,text="Eliminar", width=10, command=eliminarRegistros).grid(row=4,column=1)
        Button(groupBox,text="Actualizar", width=10, command=modificarRegistros).grid(row=4,column=2)

        #Elementos del segundo frame
        groupBox = LabelFrame(win,text="Lista del personal", padx=5,pady=5)
        groupBox.grid(row=0, column=1, padx=5, pady=5)

        #Crear un Treeview
        tree = ttk.Treeview(groupBox,columns=("Id","Nombres","Apellifos","Sexo"),show="headings",height=5)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Id")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Nombres")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Apellidos")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Sexo")

        #Mostrar los datos en la tabla treeview
        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)

        #Ejecutar la función de hacer click y mostrar el resultado en los Entry
        tree.bind("<<TreeviewSelect>>",seleccionarRegistro)

        tree.pack()

        win.mainloop()
    
    except ValueError as error:
        print("El error al mostrar la interfaz, error: {}".format(error))

formulario()
