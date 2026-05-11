import math

def resolver_cuadratica(a, b, c):
    if a == 0: # Si a = 0 ya se vuelve una ecuacion lineal 
        if b == 0:
            return [None, None]
        else:
            x = -c / b
            return [f"{x:.3f}", f"{x:.3f}"]

    discriminante = b**2 - 4*a*c

    if discriminante > 0: # Si Delta es mayor a 0, existen 2 soluciones reales distintas
        x1 = (-b + math.sqrt(discriminante)) / (2*a) # Calcula raices usando la formula
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return [f"{x1:.3f}", f"{x2:.3f}"]

    elif discriminante == 0: # Si Delta es igual a 0, existe una solucion real unica (raiz doble)
        x = -b / (2*a)
        return [f"{x:.3f}", f"{x:.3f}"]

    else: # Si Delta es menor a 0, no existen soluciones reales (raices complejas)
        return [None, None]
    
print("Ingrese el valor de los coeficientes a, b y c para la ecuacion cuadratica ax^2 + bx + c = 0")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
solucion = resolver_cuadratica(a,b,c)
print("Las soluciones de la ecuacion cuadratica son: ", solucion)