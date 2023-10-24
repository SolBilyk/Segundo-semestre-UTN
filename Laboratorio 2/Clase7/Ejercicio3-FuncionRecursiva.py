# Ejercicio 3: funcion recursiva
# imprimir numeros de 5 a 1 de manera descendente usando gunciones
# recursivas. Puede ser cualquier valor positivo, por ejemplo, si pasamos el 5 debe imprimir
# 5
# 4
# 3
# 2
# 1
# si ingresa numero negativo no imprimir nada
def imprimirDescencentes(num):
    if num >=1:
        print(num)
        imprimirDescencentes(num-1)
    elif num<0:
        print("valor incorrecto")

num=int(input("ingrese un numero: "))
imprimirDescencentes(num)