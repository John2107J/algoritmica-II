def evaluar_polinomio(x):
    return x**3 + x**2 + 2*x - 6


print("Ingrese un valor para x (o 0(cero) para salir): ")
x = int(input())

while x != 0:
    resultado= evaluar_polinomio(x)
    print("El resultado del polinomio para x=", x, " es: ", resultado)
    print("Ingrese otro valor para x (o 0(cero) para salir): ")
    x = int(input())

print("Cerrando programa...")
