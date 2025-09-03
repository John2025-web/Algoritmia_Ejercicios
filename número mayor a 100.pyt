#NOMBRE: Verificar si un número es mayor o menor que 100
#ENTRADA: Número ingresado por el usuario (decimal o entero)
#SALIDA: Mensaje indicando si el número es mayor o menor que 100
#PROCESO:
        #El usuario ingresa un número.
        #El sistema compara si el número es mayor o igual a 100.
        #Si es mayor o igual a 100, muestra el mensaje: "El número es mayor que 100".
        #Si es menor a 100, muestra el mensaje: "El número es menor que 100".

num1 = float(input("Ingrese un número: "))
if num1 >= 100:
    print("el numero es mayor que 100: ")
else: 
    print("el número es menor que 100")