# TP N°5 - Ejercicio 5
# Función para intercambiar el elemento x con el elemento anterior en la lista
# Si x es el primer elemento, la lista queda sin cambios

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from Ejercicio_1 import Nodo, ListaEnlazada


def intercambiar_con_anterior(lista, x):
    """
    Intercambia el elemento x con su elemento anterior en la lista.
    Si x es el primer elemento o no existe, la lista no se modifica.

    Estrategia: en lugar de re-enlazar nodos (complejo con ult_nodo),
    simplemente se intercambian los DATOS entre el nodo anterior y el nodo de x.
    Esto es correcto porque el enunciado habla de "intercambiar el elemento",
    no el nodo en sí.
    """
    if lista.esta_vacia():
        return

    # Si x está en la cabeza, no hacemos nada
    if lista.cabeza.dato == x:
        print(f"  '{x}' es el primer elemento. La lista no se modifica.")
        return

    # Buscar el nodo que contiene x y su anterior
    anterior = lista.cabeza
    actual = lista.cabeza.siguiente

    while actual is not None:
        if actual.dato == x:
            # Intercambiar datos entre anterior y actual
            anterior.dato, actual.dato = actual.dato, anterior.dato
            # Actualizar ult_nodo si alguno era el último
            # (los nodos no se mueven, solo sus datos, así que ult_nodo sigue apuntando
            # al mismo nodo físico — no necesita actualización)
            return
        anterior = actual
        actual = actual.siguiente

    print(f"  El elemento '{x}' no se encuentra en la lista.")


# --- Pruebas ---
if __name__ == "__main__":
    def construir(valores):
        L = ListaEnlazada()
        for v in valores:
            L.agregar(v)
        return L

    # Caso normal: intercambiar elemento del medio
    L = construir([1, 2, 3, 4, 5])
    print(f"Lista original: {L}")
    intercambiar_con_anterior(L, 3)
    print(f"Después de intercambiar 3 con anterior: {L}")  # [1, 3, 2, 4, 5]

    print()

    # Caso: intercambiar el segundo elemento
    L2 = construir([10, 20, 30])
    print(f"Lista original: {L2}")
    intercambiar_con_anterior(L2, 20)
    print(f"Después de intercambiar 20 con anterior: {L2}")  # [20, 10, 30]

    print()

    # Caso: x es el primer elemento → sin cambios
    L3 = construir([100, 200, 300])
    print(f"Lista original: {L3}")
    intercambiar_con_anterior(L3, 100)
    print(f"Después de intentar intercambiar 100 (primero): {L3}")  # sin cambios

    print()

    # Caso: x es el último elemento
    L4 = construir([5, 10, 15])
    print(f"Lista original: {L4}")
    intercambiar_con_anterior(L4, 15)
    print(f"Después de intercambiar 15 con anterior: {L4}")  # [5, 15, 10]
    print(f"ult_nodo sigue siendo: {L4.ult_nodo.dato}")

    print()

    # Caso: x no existe
    L5 = construir([1, 2, 3])
    print(f"Lista original: {L5}")
    intercambiar_con_anterior(L5, 99)
    print(f"Lista sin cambios: {L5}")