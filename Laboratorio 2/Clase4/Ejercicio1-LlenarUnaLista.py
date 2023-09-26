#Llenar una lista con los numeros del 1 al 50, luego mostrar la lista con el bucle for, los elementos deben mostrarse de la siguiente forma: 1-2-3-4-5...-50

lista = []
i = 1
while i <= 50:
    lista.append(i)
    i += 1
for i in lista:
    print(i, end = "-")
    
#Para que esto aparezca todo en una sola linea

Lista = list(range(1,51) ) #Le ponemos hasta el 50 asi en la lista incluye el 50
for i in Lista:
    print(i, end="-") 