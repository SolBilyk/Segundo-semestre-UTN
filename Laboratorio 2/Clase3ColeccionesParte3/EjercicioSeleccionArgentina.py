#La tarea consiste en ingresar elementos al diccionario llamado seleccionArgentina, lo elementos a ingresar deben ser como mínimo 4, estos elementos son los jugadores con su número de camiseta, nombre, apellido, edad, altura, precio y posición de juego, por supuesto ver el video anterior.La tarea consiste en ingresar elementos al diccionario llamado seleccionArgentina, lo elementos a ingresar deben ser como mínimo 4, estos elementos son los jugadores con su número de camiseta, nombre, apellido, edad, altura, precio y posición de juego, por supuesto ver el video anterior-

SeleccionArgentina ={
    10:{"nombre":"Lionel Messi","Edad":35,"Altura":1.70,"Precio":"50 Millones","Posicion":"Extremo Derecho"},
    11:{"nombre":"Angel Di Maria","Edad":34,"Altura":1.80,"Precio":"12 Millones","Posicion":"Extremo Derecho"},
    24:{"nombre":"Paulo Dybala","Edad":28,"Altura":1.77,"Precio":"35 Millones","Posicion":"Media Punta"},
    19:{"nombre":"Nicolas Otamendi","Edad":34,"Altura":1.83,"Precio":"3.5 Millones","Posicion":"Defensa Central"},
    1:{"nombre":"Franco Armani","Edad":35,"Altura":1.89,"Precio":"3.5 Millones","Posicion":"Portero"},
    23:{"nombre":"Emiliano Martinez","Edad":31,"Altura":1.95,"Precio":"28 Millones","Posicion":"Portero"},
    9:{"nombre":"Julian Alvarez","Edad":23,"Altura":1.70,"Precio":"60 Millones","Posicion":"Delantero"},
    20:{"nombre":"Alexis Mac Allister","Edad":24,"Altura":1.74,"Precio":"35 Millones","Posicion":"Mediocampista"},
    3:{"nombre":"Nicolas Tagliafico","Edad":31,"Altura":1.72,"Precio":"9 Millones","Posicion":"Lateral Izquierdo"}
}
for llave,valor in SeleccionArgentina.items():
    print(llave,valor)
print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end=" ")
print(len(SeleccionArgentina))