#NOMBRE: Validar contraseña para acceso
#ENTRADA: Contraseña ingresada por el usuario (cadena de texto)
#SALIDA: Mensaje indicando si el acceso fue concedido o denegado
#PROCESO:
        #El usuario ingresa una contraseña.
        #El sistema compara la contraseña ingresada con la contraseña correcta (en este caso, "password").
        #Si las contraseñas coinciden, muestra el mensaje "Acceso concedido".
        #Si no coinciden, muestra el mensaje "Acceso denegado".


clave1 = str(input("Ingrese su contraseña: "))
if clave1 == "silversoul123":
    print("Acceso concedido")
else:
    print("Acceso denegado")