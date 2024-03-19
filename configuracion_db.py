import mysql.connector

def verificar_credenciales(correo, contraseña):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",  # Usuario por defecto de XAMPP
        password="",  # Contraseña por defecto de XAMPP
        database="usuarios_db"
    )

    cursor = conexion.cursor()

    consulta = "SELECT * FROM usuarios WHERE correo = %s AND contraseña = %s"
    cursor.execute(consulta, (correo, contraseña))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado

# Ejemplo de uso
correo_ingresado = input("Ingrese su correo: ")
contraseña_ingresada = input("Ingrese su contraseña: ")

resultado = verificar_credenciales(correo_ingresado, contraseña_ingresada)

if resultado:
    print("¡Usuario correcto!")
else:
    print("Valor incorrecto")
