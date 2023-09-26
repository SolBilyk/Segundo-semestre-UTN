#TUPLA: utiliza parentesis - SON INMUTABLES
cocina = ('cuchara', 'cuchillo' , 'tenedor')
print(cocina)
print(len(cocina))

#acceder a un elemento, para esto utilizamos corchetes
print(cocina[0])
#mostrar de atras hacia adelante
print(cocina[-1])
#acceder a un rango
print(cocina[0:1]) #va a mostrar solo un lugar. recordar que siempre va a mostrar uno menos
print(cocina[0:2])

#ejemplo
verduras = ('papa',) #sin coma no es tupla, es una cadena(string). aunque se aun solo elemento necesita la coma

#recorrer los elementos de una tupla
for cocinar in cocina:
    print(cocinar) #print imprime en columna una abajo de la otra. usa por default \n para saltos de linea
    
for cocinar in cocina:    
    print(cocinar, end= ' ') #de esta manera imprime todo en una linea
    
#LAS TUPLA NO SE PUEDEN MODIFICAR, la unica manera posible es cambiarlo a lista, hacer la modificacion 
#y volverlo a tupla:

cocinalista = list(cocina)
cocinalista[0] = 'plato'
cocina = tuple(cocinalista)
print('\n',cocina)  #MALA PRACTICA!

del cocina #eliminamos la tupla

tupla = (4, 'hola', 6.78, [1,2,78], 4, 'hola')
print(tupla)
print(4 in tupla)
print(4 not in tupla)