#Ejercicio 1: Eliminar duplicados de una lista.
#Escriba un programa donde tenga una lista y que a continuacion elimine los elementos repetidos, por ultimo mostrar la lista.

#Creamos una lista (la lista es con corchetes)

Lista = [1, 2, 3, "silla", 5, 6, 5, "escritorio", 3]
print(Lista)

#Pasamos la lista a un conjunto para eliminar los elementos repetidos y los ordena por nro u orden alfabetico.

Conjunto = set(Lista)
print(Conjunto) 

#Volvemos a pasar a lista como pide el ejercicio

Lista =list(Conjunto)
print(Lista)

#Tambien se pueden hacer todos los pasos anteriores en una sola linea:

Lista = list(set(Lista))
print(Lista)
