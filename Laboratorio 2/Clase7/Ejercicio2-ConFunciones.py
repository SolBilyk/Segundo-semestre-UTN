# Ejercicio 2: funcion con * args para multiplicar crear una funcion para multiplicar los valores recibidos de tipo numerico, utilizando argumentos variabnles *args como parametro de la funcion y regresar como resultado la multiplicacion de todos los valores pasados como argumentos

def multiplicar(*numeros):
    resultado=1
    for n in numeros:
        resultado*=n
    return resultado

print(multiplicar(3, 5, 15, 3))