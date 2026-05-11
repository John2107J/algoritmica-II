# TP N°5 - Ejercicio 6
# Mezclar dos listas enlazadas ordenadas (ascendentes) en una lista ordenada descendente
# El algoritmo debe ser O(n) según la longitud de la lista de salida

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from Ejercicio_1 import Nodo, ListaEnlazada


def mezclar_descendente(lista1, lista2):
    """
    Mezcla dos listas enlazadas con elementos en orden CRECIENTE,
    y devuelve una nueva lista con todos los elementos en orden DECRECIENTE.

    Estrategia O(n):
    - Hacemos un merge de las dos listas como si quisiéramos orden ascendente,
      pero en lugar de agregar al final (lo cual daría ascendente),
      insertamos cada elemento al INICIO de la lista resultado.
    - De esta forma, al insertar en orden ascendente al inicio,
      el resultado queda en orden descendente.
    - Recorremos cada lista una sola vez → O(n1 + n2) = O(n).
    """
    resultado = ListaEnlazada()

    nodo1 = lista1.cabeza
    nodo2 = lista2.cabeza

    # Merge: en cada paso tomamos el menor de los dos punteros
    # y lo insertamos al inicio del resultado (para obtener orden decreciente)
    while nodo1 is not None and nodo2 is not None:
        if nodo1.dato <= nodo2.dato:
            resultado.agregar_al_inicio(nodo1.dato)
            nodo1 = nodo1.siguiente
        else:
            resultado.agregar_al_inicio(nodo2.dato)
            nodo2 = nodo2.siguiente

    # Procesar los nodos restantes de lista1
    while nodo1 is not None:
        resultado.agregar_al_inicio(nodo1.dato)
        nodo1 = nodo1.siguiente

    # Procesar los nodos restantes de lista2
    while nodo2 is not None:
        resultado.agregar_al_inicio(nodo2.dato)
        nodo2 = nodo2.siguiente

    return resultado


# --- Pruebas ---
if __name__ == "__main__":
    def construir(valores):
        L = ListaEnlazada()
        for v in valores:
            L.agregar(v)
        return L

    # Ejemplo del enunciado
    L1 = construir([1, 12, 45, 46])
    L2 = construir([0, 20, 40, 60, 80, 100])

    print(f"L1 = {L1}")
    print(f"L2 = {L2}")

    L3 = mezclar_descendente(L1, L2)
    print(f"L3 (mezcla descendente) = {L3}")
    # Esperado: [100, 80, 60, 46, 45, 40, 20, 12, 1, 0]

    print()

    # Caso con listas de igual longitud
    La = construir([1, 3, 5])
    Lb = construir([2, 4, 6])
    Lc = mezclar_descendente(La, Lb)
    print(f"La = {La}")
    print(f"Lb = {Lb}")
    print(f"Mezcla descendente = {Lc}")  # [6, 5, 4, 3, 2, 1]

    print()

    # Caso con una lista vacía
    Ld = ListaEnlazada()
    Le = construir([10, 20, 30])
    Lf = mezclar_descendente(Ld, Le)
    print(f"Lista vacía + {Le} = {Lf}")  # [30, 20, 10]

    print()

    # Caso con elementos duplicados en ambas listas
    Lg = construir([1, 5, 5, 10])
    Lh = construir([2, 5, 8])
    Li = mezclar_descendente(Lg, Lh)
    print(f"Lg = {Lg}")
    print(f"Lh = {Lh}")
    print(f"Mezcla descendente con duplicados = {Li}")