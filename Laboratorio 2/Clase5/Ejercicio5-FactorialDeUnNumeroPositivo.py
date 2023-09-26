#Ejercicio 5: Hacer un programa para calcular el factorial de un numero positivo

numero = int(input("Ingrese un numero:"))
while numero < 0: #Mientras el numero sea menor que cero tendremos un numero negativo y no nos sirve
    print("Error --> El numero debe ser positivo")
    numero = int(input("Ingrese nuevamente un numero: "))

#Creamos una variable llamada factorial
factorial = 1 #esta es la variable para calcular el factorial

for i in range(1, numero+1): #con el ciclo for e iterador poniendo el rango desde 1 y la variable +1 para que abarque la variable en su totalidad
    factorial *= i

print(f"\n El factorial del numero {numero} positivo ingresado es: {factorial}")
    
    