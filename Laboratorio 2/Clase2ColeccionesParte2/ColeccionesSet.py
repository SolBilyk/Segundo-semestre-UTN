#las colecciones Set no tiene un orden y no permite almacenar elementos duplicados o repetidos , no se puede modificar pero si se puede eliminar o agregar. no es completamente mutable, ni completamente inmutable
#no mantiene ningun indice, el orden es completamente aleatorio
#un elemento de tipo set es una coelccion sin orden y sin indices
#sirve para evitar elementos duplicados

planetas = {'marte', 'jupiter', 'venus'}
print(planetas)
print(len(planetas)) #la funcion len es para ver el largo

#revisar si un elemento existe dentro de set
print('marte' in planetas) #respetar mayusculas
print('marte' not in planetas)

#agregar un elemento
planetas.add('tierra') 
planetas.add('tierra') #no agrega elementos duplicados o repetidos
print(planetas)

#eliminar elemtos. puede arrojar error si el elemento no existe
planetas.remove('tierra')
print(planetas)
planetas.discard('tierra')
print(planetas)

#las dos funciones eliminan elementos. si en la funcion remove ponemos un elemento mal escrito la ejecucion saldra con error. si en la funcion discard ponemos un elemento mal escrito, es ejecutara sin ningun cambio, y no da aviso de error

#limpiar set
planetas.clear()
print(planetas)

#eliminar set
del planetas()
print(planetas)