def es_primo(n):
    if n <= 1:
        return False

    for i in range(2, n): #con range puedo establecer un rango de números, en este caso desde el 2 hasta n-1
        if n % i == 0:
            return False

    return True



while True:
    numero = int(input("Ingrese un número entero (0 para salir): "))

    if numero == 0:
        print("Saliendo del programa.")
        break
    
    if es_primo(numero):
        print("El número es primo")
    else:
        print("El número no es primo")

