def primera_y_ultima(lista_palabras):
    lista_palabras.sort() # sort() ordena la lista de menor a mayor
    return lista_palabras[0], lista_palabras[-1]



cantidad = int(input("¿Cuántas palabras desea ingresar?: "))
palabras = []

for i in range(cantidad):
    palabra = input(f"Ingrese la palabra {i+1}: ")
    palabras.append(palabra)

primera, ultima = primera_y_ultima(palabras)

print("Lista ordenada:", palabras)
print("Primera palabra:", primera)
print("Última palabra:", ultima)


