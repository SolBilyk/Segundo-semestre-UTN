#Ejercicio 1: crear una funcion para suamr los valores recibidos de tipo numericos
#utilizando argumentos variables *args como parametro de la funcion y agregar como resultado la suma de todos los valores
#pasados como argumentos

def suma(*num:int):
    res=0
    for i in num:
        res+=i
    return res
        
print(suma(5,1,3))