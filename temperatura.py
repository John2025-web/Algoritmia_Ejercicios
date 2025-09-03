#NOMBRE: Verificar estado de congelación según la temperatura
#ENTRADA: Temperatura ingresada por el usuario (número decimal)
#SALIDA: Mensaje que indica si el objeto está congelado o descongelado
#PROCESO:  
        #El usuario ingresa una temperatura.
        #Se convierte la entrada a número decimal (float).
        #Se evalúa si la temperatura es mayor o igual a 0.
        #Si es mayor o igual a 0, se muestra el mensaje "Está descongelado".
        #Si es menor que 0, se muestra el mensaje "Está congelado".

num1 = float(input("Ingrese la temperatura: "))
if num1>= 0:
    print("Esta  descongelado")
else:
    print("Esta congelado")