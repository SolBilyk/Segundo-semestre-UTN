#Ejercicio 1: Dada la siguiente tupla:
tupla = (13, 1, 8, 3, 2, 5, 8) #Definimos la tupla
#Crear una lista que solo incluya los numeros inferiores a 5 e imprima por consola [1, 3, 2]

print("La tupla es:")
print(len(tupla)) #De esta forma solo muestra la cantidad de elementos
print(tupla[0:7]) #De esta forma muestra los elementos que tiene la tupla

#Hacemos la lista
for listita in tupla:
    if listita < 5:
        print(listita)
