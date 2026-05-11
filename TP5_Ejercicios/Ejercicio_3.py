# TP N°5 - Ejercicio 3
# Método iguales() que compara dos listas enlazadas nodo a nodo

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from Ejercicio_1 import Nodo, ListaEnlazada


class ListaEnlazadaComparable(ListaEnlazada):
    """Extiende ListaEnlazada con el método iguales()."""

    def iguales(self, otra):
        """
        Compara esta lista con 'otra'.
        Dos listas son iguales si tienen los mismos datos en el mismo orden.

        Algoritmo:
        1. Comparar longitudes. Si difieren → False.
        2. Recorrer ambas listas en paralelo comparando nodo a nodo.
        3. Si algún par difiere → False.
        4. Si se recorrieron todos los nodos sin diferencias → True.
        """
        # Paso 1: comparar longitudes
        if len(self) != len(otra):
            return False

        # Paso 2 y 3: comparar nodo a nodo
        nodo_a = self.cabeza
        nodo_b = otra.cabeza
        while nodo_a is not None and nodo_b is not None:
            if nodo_a.dato != nodo_b.dato:
                return False
            nodo_a = nodo_a.siguiente
            nodo_b = nodo_b.siguiente

        # Paso 4: todos los nodos eran iguales
        return True

    def __eq__(self, otra):
        """Permite usar el operador == entre dos listas."""
        if not isinstance(otra, ListaEnlazada):
            return False
        return self.iguales(otra)


# --- Pruebas ---
if __name__ == "__main__":
    def construir(valores):
        L = ListaEnlazadaComparable()
        for v in valores:
            L.agregar(v)
        return L

    L1 = construir([1, 2, 3])
    L2 = construir([1, 2, 3])
    L3 = construir([1, 2, 4])
    L4 = construir([1, 2])
    L5 = ListaEnlazadaComparable()  # vacía
    L6 = ListaEnlazadaComparable()  # vacía

    print(f"L1 = {L1}")
    print(f"L2 = {L2}")
    print(f"L3 = {L3}")
    print(f"L4 = {L4}")
    print(f"L5 = {L5} (vacía)")
    print(f"L6 = {L6} (vacía)")
    print()

    print(f"L1.iguales(L2) → {L1.iguales(L2)}")   # True
    print(f"L1.iguales(L3) → {L1.iguales(L3)}")   # False (distinto último)
    print(f"L1.iguales(L4) → {L1.iguales(L4)}")   # False (distinta longitud)
    print(f"L5.iguales(L6) → {L5.iguales(L6)}")   # True (ambas vacías)
    print(f"L1.iguales(L5) → {L1.iguales(L5)}")   # False
    print()
    print(f"L1 == L2 → {L1 == L2}")               # True (usando __eq__)
    print(f"L1 == L3 → {L1 == L3}")               # False