from Ejercicio_6 import pedir_numero_entero #funcion de pedir entero
import math #para usar raiz con la formula de fibonacci
import time 


#Fibonacci
def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo (n-1) + fibonacci_recursivo (n-2)


def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a,b = 0,1
        for i in range(2,n+1):
            a,b = b,a+b
        return b

#Este metodo suele perder precision con numeros grandes.
def fibonacci_formula(n): #Formula de Binet F(n)= (phi^n - psi^n) / sqrt(5)
    phi = (1 + math.sqrt(5))/2 #numero aureo
    psi = (1 - math.sqrt(5))/2 #otra raiz
    return int((phi**n - psi**n) / math.sqrt(5)) #con ambos se llega a Binet.


n = pedir_numero_entero("Ingrese el número de términos de la serie de Fibonacci: ")


#Medicion de tiempo de ejecucion de funciones
inicio = time.perf_counter_ns()
fibonacci_formula(n)
fin = time.perf_counter_ns()
print (f"Tiempo de ejecucion con formula: {fin - inicio:.2f} segundos")
print()

inicio = time.perf_counter_ns()
fibonacci_recursivo(n)
fin = time.perf_counter_ns()
print (f"Tiempo de ejecucion con recursivo: {fin - inicio:.2f} nanosegundos")
print()

inicio = time.perf_counter_ns()
fibonacci_iterativo(n)
fin = time.perf_counter_ns()
print (f"Tiempo de ejecucion con iterativo: {fin - inicio:.2f} nanosegundos")
print()

#Eleji el perf_counter_ns porque mide el tiempo en nanosegundos, es mas preciso
# y en este caso al ser funciones cortas no llegan al segundo, por lo que mediria 0
#Luego process_time() mide unicamente tiempo de CPU.