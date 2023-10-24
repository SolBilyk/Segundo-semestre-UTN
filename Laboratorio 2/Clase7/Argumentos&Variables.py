def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f"{llave}: {valor}")

listarTerminos() #no pasa nada
listarTerminos(IDE="Entorno de desarrollo integrado", PK="llave primaria")
listarTerminos(Nombre= "Leo Messi") ##no acepta numero en las llaves