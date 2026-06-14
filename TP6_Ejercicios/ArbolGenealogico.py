from TadArbolB import *
from TadArbolBBusqueda import *


def pedir_nombre(mensaje):
    """Pide un nombre por consola."""
    # En caso de que no sepa la persona que se pregunta
    NO_SE = {"no sé", "no se", "nose"}

    while True:
        valor = input(mensaje).strip()

        # Respuesta "no sé"?
        if valor.lower() in NO_SE:
            return None

        # Campo vacio
        if not valor:
            print("  El nombre no puede estar vacío. Intentá de nuevo.\n")
            continue

        # Solo letras y espacios 
        if not all(c.isalpha() or c.isspace() for c in valor):
            print("  El nombre solo puede contener letras y espacios. Intentá de nuevo.\n")
            continue

        return valor.title()


#  Construccion interactiva del arbol

def cargar_genealogico(nombre, nivel=0):
    """
    Construye recursivamente el árbol genealógico preguntando
    al usuario quién es la madre y quién es el padre de 'nombre'.
    'nivel' se usa solo para indentar las preguntas y orientar al usuario.
    """
    nodo = ArbolBB(nombre)
    indent = "  " * nivel  # sangría visual según profundidad

    print(f"\n{indent}── {nombre} ──")

    # ── MADRE (hijo izquierdo) ───────────────────
    print(f"{indent}  ¿Quién es la MADRE de {nombre}?")
    print(f'{indent}  (escribí el nombre o "no sé" si no lo sabés)')
    madre = pedir_nombre(f"{indent}  Madre: ")

    if madre is not None:
        nodo.izq = cargar_genealogico(madre, nivel + 1)

    # ── PADRE (hijo derecho) ─────────────────────
    print(f"\n{indent}  ¿Quién es el PADRE de {nombre}?")
    print(f'{indent}  (escribí el nombre o "no sé" si no lo sabés)')
    padre = pedir_nombre(f"{indent}  Padre: ")

    if padre is not None:
        nodo.der = cargar_genealogico(padre, nivel + 1)

    return nodo


#  Main

def main():
    print("=" * 50)
    print("     ÁRBOL GENEALÓGICO INTERACTIVO")
    print("=" * 50)
    print()
    print('Consejo: cuando no conozcas a un nombre escribí "no se".')
    print()

    # ── Pedir nombre de la persona raíz ─────────
    raiz_nombre = pedir_nombre("Ingresá el nombre de la persona raíz: ")

    print()
    print("Ahora vas a ingresar los ancestros de cada persona.")
    print("El árbol se va construyendo de generación en generación.")

    # ── Construir el arbol 
    arbol = cargar_genealogico(raiz_nombre)

    # Resultads
    print()
    print("ARBOL GENEALOGICO GENERADO")
    print()

    print("Recorrido inorden (de izquierda a derecha):")
    print()
    arbol.imprimir()   # Se encuentra en TadArnolBBusqueda.py
    print()


if __name__ == "__main__":
    main()