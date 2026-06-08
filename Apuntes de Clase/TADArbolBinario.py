class arbolBinario:

    def __init__(self,dato,izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der
    
    def __str__(self):
        return str(self.dato)
    
    def printPrefijo(self):
        print(self, end= " ")
        if self.izq is not None:
            self.izq.printPrefijo()
        if self.der is not None:
            self.der.printPrefijo()

    def printPostfijo(self):
        if self.izq is not None:
            self.izq.printPostfijo()
        if self.der is not None:
            self.der.printPostfijo()
        print(self, end= " ")
    
    def printInfijo(self):
        if self.izq is not None:
            self.izq.printInfijo()
        print(self, end= " ")
        if self.der is not None:
            self.der.printInfijo()


""" Tamaño y Altura de un Arbol Binario"""

def sizeA(arbol):
    """Calcula el tamaño del arbol contando la cantidad de nodos"""
    """Se eligio la implemenatacion como funcion, no como metodo"""

    if arbol is None:
        return 0
    else:
        return 1 + sizeA(arbol.izq) + sizeA(arbol.der)
    
def alturaA(arbol):
    """ Calcula la altura del arbol, que es el camino  mas largo"""
    """ De la raiz a una hoja"""
    """ Se eligio la implementacion como funcion, no como metodo"""
    if arbol == None:
        return -1
    alt_izq = alturaA(arbol.izq)
    alt_der = alturaA(arbol.der)
    return 1 + max(alt_izq, alt_der)
