#listas tmb se denominan arrglos o vectores
#listas = Ariel, Liliana , Natalia

nombres = ['Ariel', 'Liliana' , 'Natalia' , 'mica'] #cada nombre ocupa un espacio
print(nombres)
print(nombres[0])
print(nombres[1]) 
print(nombres[0:2]) #de cero hasta 2, no incluye la posicion 2. es la 0 y la 1 
print(nombres[ :3]) #de cero hasta 3, no incluye la posicion 3. es la 0, la 1  y 2
print(nombres[1: ]) #desde 1 hasta el final
#modificar un valor de la lista
nombres[3] = 'juana' #cambio natalia por juana
print(nombres)
#iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('se acabaron los nombres de la lista')
    
#preguntamos cuantos nombres tiene nuestra lista
print(len(nombres))
#agregamos un elemento a la lista
nombres.append('marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
print(nombres)

#insertar un elemento en una posicion especifica
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

#eliminar un elemento de la lista
nombres.remove('Alberto')
print(nombres)

#eliminar el ultimo elemento
nombres.pop() #elimina el ultimo por default
print(nombres)

del nombres[2]
print(nombres)

#eliminar, borrar, o limpiar todos los elementos
nombres.clear()
print(nombres)

#eliminar lista
del nombres
print(nombres) #error, no se imprime porq ya fue eliminada

#concatenar listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1+lista2
print(lista3)

#agregar varios elementos a una lista
lista3.extend([7,8,9])
print(lista3)

print(lista3.index(5)) #para saber en que indice esta un elemento

#como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) #cuenta cuantos valores repetidos hay del elemento que le indicamos

#para poner al reves la lista
lista3.reverse()
print(lista3)

#multiplicar una lista repitiendo sus elementos
lista = [1,2,3] * 2
print(lista)

#metodos de ordenamiento
lista3.sort() #ordena de manera ascendente los elementos
print(lista3)

lista3.sort(reverse=True) #ordena de manera descendente los elementos
print(lista3)