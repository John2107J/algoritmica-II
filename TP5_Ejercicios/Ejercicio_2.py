# TP N°5 - Ejercicio 2
# Método imprimir() / __str__ que imprime la lista en formato Python

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
# Importo la ListaEnlazada del ejercicio 1
from Ejercicio_1 import Nodo, ListaEnlazada


class ListaEnlazadaImprimible(ListaEnlazada):

    def _imprime_lista(self, nodo):

        if nodo is None:
            return ""
        if nodo.siguiente is None:
            return str(nodo.dato)
        return str(nodo.dato) + ", " + self._imprime_lista(nodo.siguiente)

    def imprimir(self):
        """Imprime la lista en el formato [a, b, c] de Python."""
        contenido = self._imprime_lista(self.cabeza)
        print("[" + contenido + "]")

    def __str__(self):
        contenido = self._imprime_lista(self.cabeza)
        return "[" + contenido + "]"


# --- Pruebas ---
if __name__ == "__main__":
    L1 = ListaEnlazadaImprimible()

    # Lista vacía
    print("Lista vacía con print():")
    print(L1)

    L1.imprimir()

    # Agregar elementos
    L1.agregar(0)
    L1.agregar(2)
    L1.agregar(123)

    print("\nLista con elementos:")
    print(L1)
    L1.imprimir()

    # Otro ejemplo
    L2 = ListaEnlazadaImprimible()
    for val in [5, 10, 15, 20]:
        L2.agregar(val)
    print("\nOtra lista:")
    print(L2)
    L2.imprimir()