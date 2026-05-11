from Ejercicio_6 import pedir_numero_entero #funcion de pedir entero

def cuenta_atras(n):
    if n == 0:
        print("Despegando!")
    else:
        print(n)
        cuenta_atras(n - 1)



if __name__ == "__main__":
    n = pedir_numero_entero("Ingrese el número de segundos para la cuenta atrás: ")
    cuenta_atras(n)