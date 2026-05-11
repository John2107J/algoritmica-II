def mcd_euclides(a, b): #Algoritmo de Euclides
    if b == 0:
        return a
    else:
        return mcd_euclides(b, a % b)

#Creo una funcion para validar el input
#Cree una funcion para reutilizarla en otro codigo
def pedir_numero_entero(numero):
    while True:
        try:
            numero = int(input(numero))
            return numero
        except ValueError:
            print("Error: debe ingresar un numero entero.")



if __name__ == "__main__":
    a = pedir_numero_entero("Ingrese el primer numero: ")
    b = pedir_numero_entero("Ingrese el segundo numero: ")

    print("El MCD de", a, "y", b, "es:", mcd_euclides(a, b))