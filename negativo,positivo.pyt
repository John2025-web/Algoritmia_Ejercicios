# Nombre: Verificar si un número es positivo, negativo o cero
# Entrada: Número ingresado por el usuario (decimal o entero)
# Salida: Mensaje que indica si el número es positivo, negativo o cero
# Proceso:
        #El programa solicita al usuario que ingrese un número.
        #Convierte el dato ingresado a un número decimal (float).
        #Evalúa si el número es mayor que cero, menor que cero o igual a cero.
        #Si es mayor que cero, imprime “El número es positivo.”
        #Si es menor que cero, imprime “El número es negativo.”
        #Si es igual a cero, imprime “El número es cero.”



numero = float(input("Ingrese un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
