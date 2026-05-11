def sumatoria (a,b):
    if a==b:
        return b
    elif a>b: #agrego condicion para evitar recursion infinita
        return 0
    else:
        return a + sumatoria (a+1,b)


a = int (input ("Ingrese el valor de (i) en la sumatoria: "))
b = int (input ("Ingrese el valor de (n) en la sumatoria: "))

print (sumatoria(a,b))