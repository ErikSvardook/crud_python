import mysql.connector

class CConnection:
    def connectionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user="root", password="erik123",host="127.0.0.1",database="clientesdb",port="3306")
            print("Conexión correcta")
            return conexion
                                               

        except mysql.connector.Error as error:
            print("Error al conectarte a la base de datos: {}".format(error))
            return conexion
        

    connectionBaseDeDatos()
