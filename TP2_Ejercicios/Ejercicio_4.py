def cuantos_bits (n): #Divido el entero en dos hasta llegar a un cociente 0, eso me dara el total de bits de necearios
    if n==0:
        return 0
    else:
        return 1 + cuantos_bits (n//2)



n = int (input("Ingrese un valor entero: "))
print ("El numero de bits necesarios para ",n," es: ", cuantos_bits(n))