def desplegarNombres(nombres):
    for n in nombres:
        print(n)

nombres2=["Cacho", "Pablo", "Franco"]
desplegarNombres(nombres2)
desplegarNombres("Carla")

desplegarNombres((10,11)) # asi se convierte en tupla
desplegarNombres([22,55]) #asi se convierte en lista