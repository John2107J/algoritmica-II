"""Escriba una función recursiva que, dados
dos números enteros a y b, ….."""

def comparacion(a,b):
    if b == 0:
        return False
    elif a==0:
        return False
    else:
        return comparacion(a-1,b-1)
    
