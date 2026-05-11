def calculo_billetes(cantidad):
    billetes = [1000,500,200,100,50,20,10,5,2,1]
    resultado = ""

    for billete in billetes:
        if cantidad >= billete:
            num_billetes = cantidad // billete
            cantidad -= num_billetes * billete
            resultado += "Billetes de " + str(billete) + " Utiliza: " + str(num_billetes) + "\n"

    return resultado


print("Ingrese el monto a calcular: ")
print("No calcula decimales, solo billetes o monedas enteros")
cantidad = int(input())
print("Calculando billetes y monedas para: €",cantidad)
print(calculo_billetes(cantidad))