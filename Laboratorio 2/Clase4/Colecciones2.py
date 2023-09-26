# Ejercicio 2: Operaciones de conjuntos con listas.
#Escriba un programa que tenga 2 listas y que a continuacion cree las siguientes listas (en las que no deben haber repeticion):
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

Lista1 = [1, 2, 3, 4, 5, 6, 5, 4, 2, 2, 1]
Lista2 = [4, 5, 6, 7, 8, 7, 6, 5, 5, 6, 9]

# Eliminar los elementos repetidos en ambas listas con conjuntos
Conjunto1 = set(Lista1)
Conjunto2 = set(Lista2)

union = list(Conjunto1 | Conjunto2)
solo1 = list(Conjunto1 - Conjunto2) #Solo muestra el conjunto1
solo2 = list(Conjunto2 - Conjunto1) #Solo muestra el conjunto2

Interseccion = list(Conjunto1 & Conjunto2)

print(f"La lista de palabras que aparecen en las listas son: {union}")
print(f"Las listas de palabras que aparecen en la primer lista pero no en la segunda: {solo1}")
print(f"La lista de palabras que aparecen en la segunda lista pero no en la primera: {solo2}")
print(f"La lista de palabras que aparecen en ambas listas: {Interseccion}")