from Ejercicio_6 import pedir_numero_entero #funcion de pedir decimal


def combinatorio(n, m):
    if m > n:
        return print("Error: m no puede ser mayor que n por definicion.")
    elif m == 0 or m == n: 
        return 1
    else:
        return combinatorio(n - 1, m - 1) + combinatorio(n - 1, m)


#MAIN
if __name__ == "__main__":
    n = pedir_numero_entero("Ingrese el valor de n: ")
    m = pedir_numero_entero("Ingrese el valor de m: ")

    resultado = combinatorio(n, m)
    print(f"El número combinatorio ({n}, {m}) es: {resultado}")