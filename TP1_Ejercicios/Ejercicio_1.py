print("Ingrese dos numero enteros: ")
primer_numero = int(input())
print("Ingrese el segundo numero entero: ")

segundo_numero = int(input())
cubo_segundo_numero = segundo_numero ** 3

if primer_numero == cubo_segundo_numero:
    print("El primer numero es el cubo exacto del segundo")
elif primer_numero < cubo_segundo_numero:
    print("El primer numero es menor al cubo del segundo")
else:
    print("El primer numero es mayor al cubo del segundo")
