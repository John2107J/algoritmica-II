#Tad Arbol Binario
class ArbolB:
    #Creo mi arbol, con el dato
    def __init__(self,dato, izq= None, der= None):
        self.dato = dato
        self.izq = izq
        self.der = der

    def __str__(self):
        return str(self.dato)  

    def izquierdo(self, dato):
        self.izq = ArbolB(dato)

    def derecho(self, dato):
        self.der = ArbolB(dato)
    

#Funciones de árboles
def sizeA(arbol):
    """Calcula el tamaño del árbol contando la cantidad de nodos"""
    if arbol == None:
        return 0
    return 1 + sizeA(arbol.izq) + sizeA(arbol.der)

def alturaA(arbol):
    """Calcula la altura del árbol, que es el camino más largo de la raíz a una hoja"""
    if arbol == None:
        return -1
    alt_izq = alturaA(arbol.izq)
    alt_der = alturaA(arbol.der)

    return 1 + max(alt_izq, alt_der)

# Ejercicio 2
def cant_hojas(nodo):
    #Caso base: si el arbol esta vacio
    if nodo is None:
        return 0
    #Caso base: si el arbol tiene una hoja
    if nodo.izq is None and nodo.der is None:
        return 1
    #Caso recursivo
    return cant_hojas(nodo.izq) + cant_hojas(nodo.der)

# Ejercicio 4
def Es_ABB (nodo,min = float("-inf"), max = float ("inf")):

    if nodo is None:
        return True
    
    if min >= nodo.dato or max <= nodo.dato:
        return False
    
    return (Es_ABB(nodo.izq, min, nodo.dato) and Es_ABB(nodo.der, nodo.dato, max))


    

