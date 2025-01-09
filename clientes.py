from connection import *

class CClientes:

    def mostrarClientes():
        try:
            cone = CConnection.connectionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

    def ingresarClientes(nombres, apellidos, sexo):
        try:
            cone = CConnection.connectionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into usuarios values (null,%s,%s,%s);"
            #La variable valores tiene que ser una tupla
            #Como minima expresion es: (valor,) la coma hace que sea una tupla
            #Las tuplas son listas inmutables, eso quiere decir que no se puede modificar
            valores = (nombres, apellidos, sexo)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error al ingresar en la base de datos {}".format(error))
    
    def modificarClientes(id, nombres, apellidos, sexo):
        try:
            cone = CConnection.connectionBaseDeDatos()
            cursor = cone.cursor()
            sql = "update usuarios set usuarios.nombres = %s, usuarios.apellidos = %s, usuarios.sexo = %s where usuarios.id = %s;"
            
            valores = (nombres, apellidos, sexo, id)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount,"Registro actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error al actualizar en la base de datos {}".format(error))

    def eliminarClientes(id):
        try:
            cone = CConnection.connectionBaseDeDatos()
            cursor = cone.cursor()
            sql = "delete from usuarios where usuarios.id = %s;"
            
            valores = (id,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount,"Registro eliminado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error al eliminar en la base de datos {}".format(error))

