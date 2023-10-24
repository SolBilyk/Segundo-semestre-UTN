#Ejercicios 11: Agenda telefonica
#Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono, el programa tendra el siguiente menu de opciones:
    # 1. Nuevo contacto
    # 2. Borrar contacto
    # 3. Ver contactos existentes
    # 4. Salir

agenda = {}
while True:
    print("\t ..MENÚ:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Elija una opcion del menu: "))
    #hacemos una estructura if para hacer las comparativas de las opciones
    if opcion == 1: #si la opcion es igual a 1 creamos un nuevo contacto
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el numero de telefono: ")
        #Hacemos un if anidado para agregar los numeros de telefonos
        if nombre not in agenda:
            agenda[nombre] = telefono #creamos el diccionario y lo mostramos con un print
            print("El contacto ha sido agregado exitosamente")
            #en el caso de que el contacto ya haya sido agregado usamos el else
        else:
            print("Este nombre de contacto ya existe")
    elif opcion == 2:
        nombre = input("¿Cual es el nombre del contacto que desea eliminar?")
        if nombre in agenda:
            del (agenda[nombre])
            print("El contacto ha sido eliminado exitosamente")
            
        else: #si no se encontro el numero del contacto
            print("El nombre del contacto no existe")
    elif opcion == 3:
        print("Agenda de contactos")
        #recorremos la coleccion con un ciclo for
        for clave, valor in agenda.items(): #con esta funcion items mostramos los elementos
            print(f"Nombre: {clave}, Telefono: {valor}")
    elif opcion == 4: 
        print("Gracias por utilizar su agenda de contactos")
        break
    else: 
        print("Opcion incorrecta")
        print()
            
            
        
