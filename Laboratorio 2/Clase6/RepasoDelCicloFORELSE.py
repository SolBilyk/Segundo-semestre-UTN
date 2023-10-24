#Repaso del ciclo For Else

numbers = [1, 2, 3, 4, 5] #se crea la lista

for n in numbers:  #con el ciclo for se recorre la lista
    print(n)
else: #cuando termina de recorrer el for viene al else e imprime este mensaje
    print("Esto se terminó")  
    #El else siempre se ejecuta, a menos que pongamos un condicional por ej n=3 y luego un break, se ejecuta hasta el 3 y ahi queda el programa 
