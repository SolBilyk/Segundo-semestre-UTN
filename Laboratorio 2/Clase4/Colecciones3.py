# Ejercicio 3: Agregar personajes a una lista
#Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos.

# Nombre: Aragon
# Clase: Guerrero
# Raza: Dunadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Islar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo sindar

#Creamos una lista vacia
personajes = []

#Creamos diccionarios:
P = {"Nombre": "Aragon",
      "Clase": "Guerrero",
      "Raza": "Dunadan del norte"}
personajes.append(P) #Agregamos a la lista un personaje #agregamos a la lista un personaje

P = {"Nombre": "Gandalf",
      "Clase": "Mago",
      "Raza": "Islar"}
personajes.append(P)

P = {"Nombre": "Legolas",
      "Clase": "Arquero",
      "Raza": "Elfo sindar"}
personajes.append(P)

print(personajes)

