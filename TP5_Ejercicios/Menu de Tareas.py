from TAD_Actualizado import *

milista = ListaEnlazada()

seguir = True

while seguir:
    
    print("1. Agregar tareas")
    print("2. Borrar tareas")
    print("3. Mostrar tareas")
    print("4. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        descripcion = input("Ingrese la descripción de la tarea: ")
        if milista.prim is None:
            numero = 1
        else:
            numero = milista.ult_nodo.dato[0] + 1

        tarea = (numero, descripcion)
        milista.agregar(tarea)

    elif opcion == 2:
        item = int(input("Ingrese el número de item que desea borrar: "))
        n = milista.prim
        posicion = 0
        encontrado = False

        while n is not None and encontrado == False:
            if n.dato[0] == item:
                milista.devolver(posicion)
                print("Tarea borrada")
                encontrado = True
            else:
                n = n.prox
                posicion += 1
        if encontrado == False:
            print("No se encontró la tarea")

    elif opcion == 3:
        imprimirNodos(milista.prim)

    elif opcion == 4:

        print("Saliendo del programa ")
        seguir = False
    
