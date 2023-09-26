#Ejercicio 4: Hacer un programa para sumar numeros pares dentro de un rango.
#Por ejemplo: suma de numeros pares del 2 al 30:
#Resultado:   total = 240

print(f"\n Haremos una suma de un rango de numeros: \n")

#Variables para el inicio y fin de la suma
ComienzoDeRango = int(input("Ingrese los numeros desde donde quiere comenzar la suma: "))
FinalDeRango = int(input("Ingrese un numero para finalizar la suma: "))
suma = 0

#Condicion para solo sumar numeros pares
for i in range(ComienzoDeRango, FinalDeRango+1): #porque +1 para que llegue una posicion mas, porque siempre se toma un numero menos a menos que se lo especifique
    if i % 2 == 0: #numero par
        suma += i 
print(f"\n La suma de los numeros pares dentro del rango es: {suma}")


    



    



