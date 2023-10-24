#Ejercicio 10: Hacer un programa que pida una cadena por teclado, luego meter los caracteres en una lista sin repetir caracteres.

cadena = input("Ingrese una cadena: ")
lista = [] #lista varia

#ciclo for para ir asignando 
for i in cadena:
    if i not in lista: #si el caracter aun no está en la lista
        lista.append(i) #lo agregamos a la lista

print(f"\n lista de caracteres sin repetir ninguno: \n {lista}") 
