#Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3.
#Ejemplo de ejecucion: 0,3,6,9.
Numeros = [0,1,2,3,4,5,6,7,8,9,10]; 
print(Numeros)
print("Se mostraran en pantalla los numeros multiplos de 3:")
for i in range(11): #ponemos 11 porque el rango va de 1 a 10, de esta forma s eincluye al 10
    if i%3 == 0: #Si al dividir i en 3 da 0 entonces es multiplo de 3, imprimir.
        print(i) 
    
#Ejercicio 2: Crear un rango de numeros del 2 al 6 e imprimelos.
ListaDeNumeros = [2,3,4,5,6];
print("Se mostraran todos los elementos de la lista:")
for numeros in ListaDeNumeros:
    print(numeros)
    
#Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1.
Lista = [3,4,5,6,7,8,9,10];
print(Lista)
print("Se mostraran los elementos de 2 en 2:")
for i in range(3, 11, 2): #desde 3 hasta 11 (1 mas para que entre el 10) de 2 en 2
        print(i)