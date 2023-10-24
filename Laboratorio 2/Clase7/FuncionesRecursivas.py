def factorial(numero):
    if numero ==1: #caso base
        return 1
    else:
        return numero*factorial(numero-1) #Caso recursivo
    
resultado = factorial(5)
print(f"el factorial de 5 es: {resultado}")