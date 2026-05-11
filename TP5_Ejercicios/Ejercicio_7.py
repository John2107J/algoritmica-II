# TP N°5 - Ejercicio 7
# TAD ListaDeAlumnos - Lista Doblemente Enlazada
# a) Método agregar_final() para añadir notas de examen con validación
# b) Programa que busca un alumno por número e imprime sus datos completos

# ── Diccionario de materias válidas ──────────────────────────────────────────
MATERIAS = {
    "MAT1": "Matemática I",
    "MAT2": "Matemática II",
    "FIS1": "Física I",
    "FIS2": "Física II",
    "ALG1": "Algorítmica y Programación I",
    "ALG2": "Algorítmica y Programación II",
    "SIS1": "Sistemas Operativos",
    "BD01": "Bases de Datos",
}

# ── Nodo de alumno (doblemente enlazado) ─────────────────────────────────────

class NodoAlumno:
    def __init__(self, numero, dni, apellido, nombre, carrera):
        self.numero = numero        # Legajo
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.carrera = carrera
        self.finales = []           # Lista de dicts: {codigo, fecha, nota, resultado}
        self.siguiente = None
        self.anterior = None

    # ── Método a) ─────────────────────────────────────────────────────────────
    def agregar_final(self, codigo_materia, fecha, nota):
        """
        Agrega una nota de examen final al alumno.

        Validaciones:
        - La nota debe estar entre 0 y 10 (inclusive). None representa ausencia.
        - El código de materia debe existir en el diccionario MATERIAS.

        El campo resultado se determina así:
        - None o -1  → "Ausente"
        - 0 a 3      → "Desaprobado"
        - 4 a 10     → "Aprobado"
        """
        if codigo_materia not in MATERIAS:
            raise ValueError(
                f"La materia '{codigo_materia}' no existe en el diccionario de materias."
            )

        if nota is None:
            resultado = "Ausente"
        elif isinstance(nota, (int, float)) and 0 <= nota <= 10:
            resultado = "Aprobado" if nota >= 4 else "Desaprobado"
        else:
            raise ValueError(
                f"Nota inválida: '{nota}'. Debe ser un número entre 0 y 10, o None para Ausente."
            )

        self.finales.append({
            "codigo":    codigo_materia,
            "materia":   MATERIAS[codigo_materia],
            "fecha":     fecha,
            "nota":      nota if nota is not None else "-",
            "resultado": resultado,
        })

    def proximo(self):
        return self.siguiente

    def previo(self):
        return self.anterior

    def imprimir(self):
        print(f"  Legajo  : {self.numero}")
        print(f"  DNI     : {self.dni}")
        print(f"  Alumno  : {self.apellido}, {self.nombre}")
        print(f"  Carrera : {self.carrera}")
        if not self.finales:
            print("  Finales : (sin finales rendidos)")
        else:
            print("  Finales :")
            print(f"    {'Código':<8} {'Materia':<35} {'Fecha':<12} {'Nota':<6} {'Resultado'}")
            print(f"    {'-'*8} {'-'*35} {'-'*12} {'-'*6} {'-'*12}")
            for f in self.finales:
                print(
                    f"    {f['codigo']:<8} {f['materia']:<35} "
                    f"{f['fecha']:<12} {str(f['nota']):<6} {f['resultado']}"
                )


# ── TAD ListaDeAlumnos ───────────────────────────────────────────────────────

class ListaDeAlumnos:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._cantidad = 0

    def cantidad(self):
        return self._cantidad

    def esta_vacia(self):
        return self.cabeza is None

    def insertar(self, numero, dni, apellido, nombre, carrera):
        """Inserta un alumno manteniendo orden por número de alumno (legajo)."""
        nuevo = NodoAlumno(numero, dni, apellido, nombre, carrera)

        # Lista vacía
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
            self._cantidad += 1
            return

        # Insertar al inicio
        if numero < self.cabeza.numero:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
            self._cantidad += 1
            return

        # Buscar posición de inserción
        actual = self.cabeza
        while actual is not None and actual.numero < numero:
            actual = actual.siguiente

        if actual is None:
            # Insertar al final
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        else:
            # Insertar antes de 'actual'
            anterior = actual.anterior
            nuevo.siguiente = actual
            nuevo.anterior = anterior
            anterior.siguiente = nuevo
            actual.anterior = nuevo

        self._cantidad += 1

    def buscar(self, numero):
        """Devuelve el NodoAlumno con ese legajo, o None si no existe."""
        actual = self.cabeza
        while actual is not None:
            if actual.numero == numero:
                return actual
            if actual.numero > numero:
                break
            actual = actual.siguiente
        return None

    def borrar(self, numero):
        """Elimina y devuelve el alumno con ese legajo. Lanza ValueError si no existe."""
        nodo = self.buscar(numero)
        if nodo is None:
            raise ValueError(f"No existe un alumno con legajo {numero}.")

        if nodo.anterior:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.cabeza = nodo.siguiente

        if nodo.siguiente:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self.cola = nodo.anterior

        nodo.siguiente = None
        nodo.anterior = None
        self._cantidad -= 1
        return nodo

    def imprimir_lista(self):
        """Imprime los datos básicos de cada alumno."""
        if self.esta_vacia():
            print("  (Lista vacía)")
            return
        actual = self.cabeza
        while actual is not None:
            print(f"  [{actual.numero}] {actual.apellido}, {actual.nombre} — DNI: {actual.dni} — Carrera: {actual.carrera}")
            actual = actual.siguiente


# ── Programa principal: parte b) ─────────────────────────────────────────────

def programa_buscar_alumno(lista):
    """Solicita un número de alumno e imprime sus datos completos."""
    print("\n══════════════════════════════════════════")
    print("      CONSULTA DE ALUMNO POR LEGAJO       ")
    print("══════════════════════════════════════════")
    try:
        legajo = int(input("Ingresá el número de alumno (legajo): ").strip())
    except ValueError:
        print("  ✗ Debés ingresar un número entero.")
        return

    alumno = lista.buscar(legajo)
    if alumno is None:
        print(f"  ✗ El alumno con legajo {legajo} NO existe en la lista.")
    else:
        print(f"\n  ── Datos del alumno ──")
        alumno.imprimir()


# ── Demo / Pruebas ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    lista = ListaDeAlumnos()

    # Insertar alumnos
    lista.insertar(1042, "38100200", "García", "Ana", "Ingeniería en Sistemas")
    lista.insertar(987,  "35000111", "López",  "Juan", "Ingeniería Civil")
    lista.insertar(1500, "40222333", "Pérez",  "María", "Ingeniería en Sistemas")
    lista.insertar(210,  "30999888", "Ruiz",   "Carlos", "Ingeniería Electrónica")

    print("=== Lista de alumnos (orden por legajo) ===")
    lista.imprimir_lista()

    # Agregar finales usando el método agregar_final (parte a)
    alumno_garcia = lista.buscar(1042)
    alumno_garcia.agregar_final("ALG1", "2025-03-15", 8)
    alumno_garcia.agregar_final("MAT1", "2025-07-10", 3)
    alumno_garcia.agregar_final("FIS1", "2025-11-20", None)  # Ausente

    alumno_lopez = lista.buscar(987)
    alumno_lopez.agregar_final("MAT1", "2025-04-05", 6)
    alumno_lopez.agregar_final("FIS1", "2025-08-18", 2)

    # Probar validaciones de agregar_final
    print("\n=== Pruebas de validación ===")
    try:
        alumno_garcia.agregar_final("XXX99", "2025-01-01", 7)
    except ValueError as e:
        print(f"  ✗ Error esperado (materia inválida): {e}")

    try:
        alumno_garcia.agregar_final("MAT2", "2025-01-01", 11)
    except ValueError as e:
        print(f"  ✗ Error esperado (nota fuera de rango): {e}")

    # Imprimir un alumno con sus finales
    print("\n=== Datos completos de Ana García (legajo 1042) ===")
    alumno_garcia.imprimir()

    print("\n=== Datos completos de Juan López (legajo 987) ===")
    alumno_lopez.imprimir()

    # Parte b): buscar alumno interactivamente
    programa_buscar_alumno(lista)