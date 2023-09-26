#Ejercicio 7: Realizar un juego para adivinar un numero. Para ello se debe generar un numero aleatorio entre el 1 - 100 y luefo ir pidiendo numeros indicando "es mayor" o "es menor" segun sea mayor o menor con respecto a N. El proceso se termina cuando el usuario acierta y alli se debe mostrar el numero de intentos.

import random

print("\t JUEGUEMOS A ADIVINAR EL NUMERO!!")

aleatorio = random.randint(0, 100) #toma los numeros desde el cero al 100
contador = 0
while True: 
    numero = int(input("Ingrese un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\n No es el numero, ingrese uno menor\n")
    elif numero < aleatorio:
        print("\n No es el numero, ingrese uno mayor\n")
    else:
        print(f"FELICITACIONES!!! acaba de adivinar el numero {aleatorio}")
        break        
print(f"\n Numero de intentos: {contador}\n") 