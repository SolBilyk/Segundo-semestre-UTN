#Desempaquetado de listas

#creamos una funcion llamada show y colocamos dos parametros:
def show(name, lastName):
    print(name + " " + lastName)
person = ["Maria", "Sol"]
show(person[0], person[1]) #pasamos uno por uno los datos de la lista a la funcion
#se van agregando los valores a los parametros
show(*person) #esto es lo mismo que lo anterior pero le pasamos todo junto

#tuplas
person2 = ("Osvaldo", "Franco") #desempaquetamos a traves de una tupla
show(*person2) 

#diccionarios
person3 = {"lastName": "Honguito", "name": "Pepito"}
show(**person3)