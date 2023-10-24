#Paso de argunemtos de funciones
def miFuncion(name,lastname): #Parametros: variables que declaramos en la funcion
    print("Saludos a todos")
    print(f"nombre:{name},Apellido: {lastname}")

miFuncion("Jorge","Lucero") #Argumentos: los valores que le pasamos a las variables de la funcion
miFuncion("Ariel","Betancud")
miFuncion("Analia","Pedrosa")

#Palabra Return
def suma(a,b):
    return a+b
resultado=suma(78,22)

print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {suma(55,75)}")

#Valores por Default
def sumar2(a:int=0,b:int=0)->int: #Se declaran los valores por defecto de las variables
    return a+b

resultado2=sumar2()
print(f"El resultado de la suma es: {resultado2}")
print(f"el resultado de la suma es: {sumar2(22,66)}")

#Argumentos Variables en funciones
def listaNombres(*nombres): #Cuando no se sabe el numero de argumentos que se vana recibir se unsa el *
    for i in nombres: #Se convierte en una tupla
        print(i)

listaNombres("lucas","jose","claudia","rosa","maria")
listaNombres("Marcos","daniel", "romina","pepe", "marcela","carlos" )