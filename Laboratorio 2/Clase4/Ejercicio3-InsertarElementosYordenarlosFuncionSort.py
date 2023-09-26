#Ejercicio 3: Pedir numeros y meterlos a una lista, cuando el usuario introduzca el numero 0 nuestro programa dejaria de insertar. Por ultimo mostrar los numeros ordenados de menor a mayor.

#Creamos una lista vacia 
lista = []

#Creamos una bandera 
salir = False #Se escribe con mayuscula

#Creamos la condicion:
while not salir: #El not cambia el valor de falso, lo cambia a lo contrario entonces le estamos diciendo mientras salir sea verdadero... 
    numero = int(input("Ingrese un numero: "))
    if numero == 0: #Si el numero es igual a 0 entonces se detiene todo, hacemos un salir:
        salir = True 
    else:  #sino, si el numero no es un cero, me va a mostrar la lista de menor a mayor.
        lista.append(numero) 
        
#En python hay una funcion para ordenar, que es sort
lista.sort()

print(f"\n Lista ordenada: \n {lista}")
        
