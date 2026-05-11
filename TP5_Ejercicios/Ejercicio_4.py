# TP N°5 - Ejercicio 4
# Programa para administrar una lista de tareas pendientes usando el TAD ListaEnlazada

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from Ejercicio_1 import Nodo, ListaEnlazada


class Tarea:
    """Representa una tarea pendiente con número de ítem y descripción."""

    def __init__(self, numero, descripcion):
        self.numero = numero
        self.descripcion = descripcion

    def __str__(self):
        return f"[{self.numero}] {self.descripcion}"

    def __eq__(self, otra):
        """Permite comparar tareas por número de ítem."""
        if isinstance(otra, Tarea):
            return self.numero == otra.numero
        return False


class ListaTareas(ListaEnlazada):
    """Extiende ListaEnlazada para manejar tareas pendientes."""

    def __init__(self):
        super().__init__()
        self._proximo_numero = 1  # Contador automático de ítems

    def agregar_tarea(self, descripcion):
        """Agrega una tarea al final con número generado automáticamente."""
        nueva_tarea = Tarea(self._proximo_numero, descripcion)
        self.agregar(nueva_tarea)
        self._proximo_numero += 1
        print(f"  ✓ Tarea agregada: {nueva_tarea}")

    def borrar_tarea(self, numero):
        """Borra la tarea con el número de ítem indicado."""
        actual = self.cabeza
        while actual is not None:
            if actual.dato.numero == numero:
                self.eliminar(actual.dato)
                print(f"  ✓ Tarea #{numero} eliminada.")
                return
            actual = actual.siguiente
        print(f"  ✗ No existe una tarea con el número {numero}.")

    def listar_tareas(self):
        """Muestra todas las tareas pendientes en orden."""
        if self.esta_vacia():
            print("  (No hay tareas pendientes)")
            return
        actual = self.cabeza
        while actual is not None:
            print(f"  {actual.dato}")
            actual = actual.siguiente


def menu():
    lista = ListaTareas()
    opciones = {
        "1": "Agregar tarea",
        "2": "Borrar tarea",
        "3": "Listar tareas",
        "4": "Salir",
    }

    while True:
        print("\n╔══════════════════════════════╗")
        print("║   ADMINISTRADOR DE TAREAS    ║")
        print("╠══════════════════════════════╣")
        for clave, descripcion in opciones.items():
            print(f"║  {clave}. {descripcion:<26}║")
        print("╚══════════════════════════════╝")
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            desc = input("  Descripción de la tarea: ").strip()
            if desc:
                lista.agregar_tarea(desc)
            else:
                print("  ✗ La descripción no puede estar vacía.")

        elif opcion == "2":
            try:
                num = int(input("  Número de ítem a borrar: "))
                lista.borrar_tarea(num)
            except ValueError:
                print("  ✗ Ingresá un número válido.")

        elif opcion == "3":
            print("\n  --- Tareas pendientes ---")
            lista.listar_tareas()

        elif opcion == "4":
            print("  ¡Hasta luego!")
            break

        else:
            print("  ✗ Opción inválida. Elegí entre 1 y 4.")


if __name__ == "__main__":
    menu()