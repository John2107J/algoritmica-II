from TadArbolBE import *

# Ejercicio 7
# Se encuentra en TadArbolBE.py

abe = ArbolBE('+')

abe.izq = ArbolBE(3)
abe.der = ArbolBE('*')

abe.der.izq = ArbolBE(4)

abe.der.der = ArbolBE('/')
abe.der.der.izq = ArbolBE(6)
abe.der.der.der = ArbolBE(7)

print("Resultado: ",abe.Evaluar())