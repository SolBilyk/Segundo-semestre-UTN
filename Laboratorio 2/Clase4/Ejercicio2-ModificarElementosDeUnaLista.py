#Ejercicio 2: Modificar los elementos de una lista
#Llenar una lista con los numeros del 1 al 10, luego modificar los elementos de la lista multiplicandolos por un valor ingresado por el usuario.

lista = list(range(1,11)) 
#armamos la lista original
print("lista original")


for i in lista:
    print(i, end = "-")

valor = int(input("\nIngrese un valor para la multiplicacion: "))
#esta es la variable que vamos a usar para que se multipliquen los numeros de la lista

#Multiplicamos todos los elementos de la lista con un for, usando una funcion especial(porque el iterador solo recorre cada indice, no puede aplicar ninguna funcion como multiplicar en este caso) es la funcion enumerate

for indice, i in enumerate(lista):
    lista[indice] *= valor
    
print(f"Lista final con los elementos multiplicados que ingreso el usuario: {valor}")
for i in lista:
    print(i, end = "-")
