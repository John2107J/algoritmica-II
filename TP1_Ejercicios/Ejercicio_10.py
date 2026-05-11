def nombres_por_letra(lista_nombres, letra):
    resultado = []

    for nombre in lista_nombres:
        if nombre[0].lower() == letra.lower():
            resultado.append(nombre)

    return resultado



nombres = []

cantidad = int(input("¿Cuántos nombres querés ingresar?: "))

for i in range(cantidad):
    nombre = input(f"Ingresá el nombre {i + 1}: ")
    nombres.append(nombre)

letra = input("Ingresá la letra por la que deben empezar: ")

lista_filtrada = nombres_por_letra(nombres, letra)

print("Nombres encontrados:", lista_filtrada)