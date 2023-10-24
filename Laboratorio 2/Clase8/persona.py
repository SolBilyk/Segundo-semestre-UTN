class Persona: #Se crea una clase
    
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
    def mostrarDetalle(self): #self solo se encuentra dentro de los metodos
        print(f"persona:{self.nombre} {self.apellido} {self.edad}")
        
#el constuctor va directamente al init
persona1=Persona("Ariel","Betancud",40) #enviamos argumentos
print(f"el objeto de la clase persona2: {persona1.nombre} {persona1.apellido} {persona1.edad}")

persona2=Persona("Juan","Belich",34)
print(f"el objeto de la clase persona2: {persona2.nombre} {persona2.apellido} {persona2.edad}")

persona1.nombre="liliana"
persona1.apellido="Buccella"
persona1.edad=40
print(f"el objeto1 modificado de la clase persona2: {persona1.nombre} {persona1.apellido} {persona1.edad}")

#Los atributos son las caracteristicas

#Los metodos son el comportamiento que van a tener los objetos, o sea las acciones

#Acá usamos el metodo mostrar detalle
persona1.mostrarDetalle()
persona2.mostrarDetalle()