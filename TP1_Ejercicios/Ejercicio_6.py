from Ejercicio_0 import intercalar

def es_alfabetica(palabra):
    palabra = palabra.lower()

    for i in range(len(palabra) - 1):
        if palabra[i] > palabra[i + 1]:
            return False

    return True


while True:
    palabra = input("Ingrese una palabra (0 para salir): ")

    if palabra == "0":
        print("Saliendo del programa.")
        break

    if es_alfabetica(palabra):
        print("La palabra es alfabética")
    else:
        print("La palabra no es alfabética")


