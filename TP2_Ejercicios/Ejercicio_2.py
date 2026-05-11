def sumatoria (n):
    if n==1:
        return 1
    else:
        return n + sumatoria (n-1)


n = int (input ("ingrese un numero entero positivo: "))
print (sumatoria(n))

