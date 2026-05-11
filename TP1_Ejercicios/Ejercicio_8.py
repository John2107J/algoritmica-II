def decodificar_texto(texto, n):
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numeros = "0123456789"

    resultado = ""

    for caracter in texto:
        if caracter in minusculas:
            pos = minusculas.index(caracter)
            nueva_pos = (pos - n) % len(minusculas)
            resultado += minusculas[nueva_pos]

        elif caracter in mayusculas:
            pos = mayusculas.index(caracter)
            nueva_pos = (pos - n) % len(mayusculas)
            resultado += mayusculas[nueva_pos]

        elif caracter in numeros:
            pos = numeros.index(caracter)
            nueva_pos = (pos - n) % len(numeros)
            resultado += numeros[nueva_pos]

        else:
            resultado += caracter

    return resultado

# Igual al ejercicio anterior pero con dezplazamiento negativo
while True:
    texto = input("Ingrese el texto cifrado (0 para salir): ")
    if texto == "0":
        print("Saliendo del programa.")
        break

    n = int(input("Ingrese el valor de n: "))

    print("Texto original:", decodificar_texto(texto, n))

