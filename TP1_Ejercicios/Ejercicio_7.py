def cifrar_texto(texto, n):
    minusculas = "abcdefghijklmnñopqrstuvwxyz" #defino el alfabeto porque en codigo ASCII la ñ se encuentra por ultimo
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" #uso dos variables de alfabeto en vez de upper o lower porque me alteraria el orden de cifrado
    numeros = "0123456789"

    resultado = ""

    for caracter in texto:
        if caracter in minusculas:
            pos = minusculas.index(caracter)
            nueva_pos = (pos + n) % len(minusculas)
            resultado += minusculas[nueva_pos]

        elif caracter in mayusculas:
            pos = mayusculas.index(caracter)
            nueva_pos = (pos + n) % len(mayusculas)
            resultado += mayusculas[nueva_pos]

        elif caracter in numeros:
            pos = numeros.index(caracter)
            nueva_pos = (pos + n) % len(numeros)
            resultado += numeros[nueva_pos]

        else:
            resultado += caracter

    return resultado


while True:
    texto = input("Ingrese un texto (0 para salir): ")
    
    if texto == "0":
        print("Saliendo del programa.")
        break

    n = int(input("Ingrese el desplazamiento: "))

    print("Texto cifrado:", cifrar_texto(texto, n))


