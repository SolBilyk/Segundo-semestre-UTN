#Videos Clase 3
#Video1
#Repaso de set o conjunto
#Definir
conjunto1 =set()
conjunto2 = {"bye",}
conjunto1.add(7)
conjunto1.add("Hola")
print(conjunto1)
conjunto2.add("hola")
print(conjunto2)
print(3 not in conjunto2) # preguntamos si el numero tres esta en conjunto2
print(conjunto2 == conjunto1)

# Video2
#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # este simbolo une los dos conjuntos |
print(conjunto3)
conjunto3 = conjunto1 & conjunto2 # que elemento tienen en comun
print(conjunto3)
conjunto3 = conjunto1 - conjunto2 # asigna el valor que esta en el conjunto1 y no esta en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1 # asigna el valor que esta en el conjunto2 pero no esta en el conjunto1
print(conjunto3)
conjunto3 = conjunto1 ^ conjunto2 # elementos que estan en los dos cunjunto pero no estan compartidos
print(conjunto3)

#Video3
conjunto3 = conjunto1 | conjunto2 
print(conjunto1.issubset(conjunto3)) # preguntamos si el conjunto1 es un subconjunto del conjunto3
print(conjunto2.issubset(conjunto3)) # preguntamos si el conjunto2 es un subconjunto del conjunto3
print(conjunto3.issubset(conjunto1)) # false el 3 no es subconjunto del 2
print(conjunto3.issubset(conjunto2)) # false el 3 no es subconjunto del 1

print(conjunto3.issuperset(conjunto1)) # preguntamos si el 3 es superconjunto del 1 (verdadero)
print(conjunto3.issuperset(conjunto2)) # verdadero idem logica que el aneterior
print(conjunto2.issuperset(conjunto3)) #false el 2 no es superconjunto del 3

#como saber si son disconexos (no comparten elementos)
print(conjunto1.isdisjoint(conjunto2)) # no hay cosas en comun
# convertir un conjunto en inmutable
conjunto1 = frozenset # no se pueden agregar quitar ni modificar elementos del conjunto