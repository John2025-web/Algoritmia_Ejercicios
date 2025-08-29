#NOMBRE: Determinar el tipo de triángulo según sus lados
#ENTRADA:
        #Lado 1 (número decimal)
        #Lado 2 (número decimal)
        #Lado 3 (número decimal)
#SALIDA: Mensaje que indica si el triángulo es equilátero, isósceles o escaleno
#PROCESO:
        #El usuario ingresa las longitudes de los tres lados del triángulo.
        #Se comparan los lados para determinar su igualdad.
        #Si los tres lados son iguales, se imprime "El triángulo es equilátero".
        #Si sólo dos lados son iguales, se imprime "El triángulo es isósceles".
        #Si los tres lados son diferentes, se imprime "El triángulo es escaleno".


num1=float(input("Ingrese el lado 1: "))
num2=float(input("Ingrese el lado 2: "))
num3=float(input("Ingrese el lado 3: "))
if num1 == num2 and num2 == num3:
    print("El triangulo es equilatero. ")
elif num1== num2 or num2==num3 or num1==num3:
    print("El triangulo es isocéles")
else:
    print("El triangulo es escaleno")