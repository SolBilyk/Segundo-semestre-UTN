#un diccionario esta compuesto por dos elementos: una llave y un valor
#dict(key, value)
diccionario = {
    'IDE': 'integrated development environment',
    'POO': 'programacion orientada a objetos',
    'SABD': 'sistema de administracion de base de datos'
}
print(diccionario)

#largo del diccionario
print(len(diccionario))

#acceder a un diccionario con la llave
print(diccionario['IDE'])

#forma de recuperar un elemento
print(diccionario.get('POO'))

#modificar elementos
diccionario['IDE'] = 'Entorno de desarrollo integrado'
print(diccionario)

#recorrer elementos del diccionario
for termino in diccionario:
    print(termino)
    
# for termino, valor in diccionario:
#     print(termino, valor) no se puede acceder de manera directa

#neccesitamos una funcion para recorrer el diccionario
for termino, valor in diccionario.items():
    print(termino, valor)
    
#otras maneras de acceder al diccionarios
for termino in diccionario.keys():
    print(termino) #muestra solo las llaves

for valor in diccionario.values():
    print(valor)
    
#comprobar la existencia de algun elemento
print('IDE' in diccionario)
print('IDE' not in diccionario)

#agregar un elemento 
diccionario['PK'] = 'primary key'
print(diccionario) 

#eliminar un elemento
diccionario.pop('SABD')
print(diccionario) 

#vaciar un diccionario
diccionario.clear()
print(diccionario) 

#eliminar diccionaio
del diccionario
print(diccionario) 