#Calcular la raiz cuadrada de un numero positivo

import math 
#tenemos que importar la clase math para hacer uso de la funcion sqrt(raiz cuadrada)

numero = int(input("Ingrese un numero positivo: "))
while numero < 0:
    print("ERROR!! Debe ingresar un numero positivo.")
    numero = int(input("Ingrese un numero positivo: "))

print(f"\nSu raiz cuadrada es:{math.sqrt(numero):.2f}") #ese 2f es para que no nos de un numero tan largo el resultado de la raiz cuadrada.


