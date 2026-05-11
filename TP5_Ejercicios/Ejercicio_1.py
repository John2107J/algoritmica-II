# TP N°5 - Ejercicio 1
# TAD ListaEnlazada con atributo ult_nodo y métodos: __str__, __len__, agregar, eliminar, indice

"""
Ventajas de agregar ult_nodo:
- Agregar al final es O(1) en vez de O(n), porque ya tenemos referencia directa al último nodo.
- Consultar directamente el ultimo nodo

Desventajas de agregar ult_nodo:
- Hay que mantener ult_nodo actualizado en TODOS los métodos que modifican la lista
  (agregar, eliminar, etc.)
- Ocupa un poco más de memoria (una referencia extra).
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.ult_nodo = None
        self._len = 0

    def __len__(self):
        return self._len

    def __str__(self):
        if self.cabeza is None:
            return "[]"
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "[" + ", ".join(elementos) + "]"

    def esta_vacia(self):
        return self.cabeza is None

    def agregar(self, x):
        """Agrega x al final de la lista."""
        nuevo = Nodo(x)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.ult_nodo = nuevo
        else:
            self.ult_nodo.siguiente = nuevo
            self.ult_nodo = nuevo
        self._len += 1

    def agregar_al_inicio(self, x):
        """Agrega x al inicio de la lista."""
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        if self.ult_nodo is None:
            self.ult_nodo = nuevo
        self._len += 1

    def eliminar(self, x):
        """Elimina la primera ocurrencia de x en la lista. Lanza ValueError si no existe."""
        if self.cabeza is None:
            raise ValueError(f"{x} no está en la lista")

        # Caso: el dato está en la cabeza
        if self.cabeza.dato == x:
            if self.cabeza == self.ult_nodo:
                # Era el único nodo
                self.ult_nodo = None
            self.cabeza = self.cabeza.siguiente
            self._len -= 1
            return

        # Buscar el nodo anterior al que queremos eliminar
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual is not None:
            if actual.dato == x:
                anterior.siguiente = actual.siguiente
                if actual == self.ult_nodo:
                    self.ult_nodo = anterior
                self._len -= 1
                return
            anterior = actual
            actual = actual.siguiente

        raise ValueError(f"{x} no está en la lista")

    def indice(self, x):
        """Devuelve el índice (base 0) de la primera ocurrencia de x. Lanza ValueError si no existe."""
        actual = self.cabeza
        i = 0
        while actual is not None:
            if actual.dato == x:
                return i
            actual = actual.siguiente
            i += 1
        raise ValueError(f"{x} no está en la lista")

    def obtener(self, i):
        """Devuelve el dato en la posición i (base 0)."""
        if i < 0 or i >= self._len:
            raise IndexError("Índice fuera de rango")
        actual = self.cabeza
        for _ in range(i):
            actual = actual.siguiente
        return actual.dato


# --- Pruebas ---
if __name__ == "__main__":
    L = ListaEnlazada()
    print("Lista vacía:", L)
    print("Longitud:", len(L))

    L.agregar(10)
    L.agregar(20)
    L.agregar(30)
    L.agregar(40)
    print("Después de agregar 10, 20, 30, 40:", L)
    print("Longitud:", len(L))
    print("ult_nodo:", L.ult_nodo.dato)

    print("Índice de 20:", L.indice(20))
    print("Índice de 40:", L.indice(40))

    L.eliminar(20)
    print("Después de eliminar 20:", L)
    print("Longitud:", len(L))

    L.eliminar(40)
    print("Después de eliminar 40 (último):", L)
    print("ult_nodo ahora:", L.ult_nodo.dato)

    L.eliminar(10)
    print("Después de eliminar 10 (primero):", L)
    print("Longitud:", len(L))

    L.eliminar(30)
    print("Después de eliminar 30 (único restante):", L)
    print("ult_nodo es None:", L.ult_nodo is None)

    try:
        L.eliminar(99)
    except ValueError as e:
        print("Error esperado:", e)