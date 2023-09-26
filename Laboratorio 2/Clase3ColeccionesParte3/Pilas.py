#Video6
#Pilas usando Listas
pila=[1,2,3]
#agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)
# sacar elementos por el final
elementoBorrado = pila.pop() # quita el ultimo elemento y lo guarda en una variable
print(f"sacamos el elemento {elementoBorrado}")
print(f"Y la pila ahora quedo asi:{pila}")