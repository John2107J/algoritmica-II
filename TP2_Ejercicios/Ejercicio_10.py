from Ejercicio_6 import pedir_numero_entero #funcion de pedir entero

def es_primo(n, divisor=2):
    if n <= 1: #caso si ingresa 1 o 0
        return False
    if divisor == n:
        return True
    if n % divisor == 0: #caso si no es primo.
        return False
    return es_primo(n, divisor + 1)

if __name__ == "__main__":
    numero = pedir_numero_entero("Ingrese un número entero: ")
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")