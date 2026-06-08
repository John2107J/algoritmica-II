class ArbolBB:
    def __init__(self, dato, izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der

    def izquierdo(self, dato):
        self.izq = ArbolBB(dato)

    def derecho(self, dato):
        self.der = ArbolBB(dato)
        
    def __str__(self):
        return str(self.dato)

    def insertar(self,x):
        """Insertamos el valor x en un ABB"""
        """En el peor caso, el arbol tiene un único nodo"""
        if x < self.dato:
            #Insertar en subárbol izquierdo
            if self.izq == None:
                self.izq = ArbolBB(x)
            else:
                self.izq.insertar(x)
        else:
            #Insertar en subárbol derecho
            if self.der == None:
                self.der = ArbolBB(x)
            else:
                self.der.insertar(x)

    def buscar(self,x):
        """Busca el nodo con valor x en el Arbol, y lo devuelve"""
        """Si ningun nodo tiene dicho dato, devuelve None"""
        dev = None
        if self.dato == x:
            dev = self
        elif x < self.dato and self.izq is not None:
            dev = self.izq.buscar(x)
        elif x> self.dato and self.der is not None:
            dev = self.der.buscar(x)
        return dev
    
    def imprimir(self):
        """Recorre e imprime creciente en orden los nodos de un ABB"""
        if self.izq is not None:
            self.izq.imprimir()
        print(self, end = " ")
        if self.der is not None:
            self.der.imprimir()
    
    def imprimirReves(self):
        if self.der is not None:
            self.der.imprimirReves()
        print(self, end =" ")
        if self.izq is not None:
            self.izq.imprimirReves()

    def minimo(self):
        minx = self
        
        while minx.izq is not None:
            minx = minx.izq
        return minx
        
    def maximo(self):
        maxn = self
        while maxn.der is not None:
            maxn = maxn.der
        return maxn
    
    # Ejercicio 5 
    def BorrarNodo(self, x):
        

        if x < self.dato:
            if self.izq is not None:
                self.izq = self.izq.BorrarNodo(x)
            return self

        elif x > self.dato:
            if self.der is not None:
                self.der = self.der.BorrarNodo(x)
            return self

    # Encontró el nodo a borrar

    # para borrar hoja
        if self.izq is None and self.der is None:
            return None

    # un hijo derecho
        if self.izq is None:
            return self.der

    #  un hijo izquierdo
        if self.der is None:
            return self.izq

    # para 2 hijos
        sucesor = self.der.minimo()
        self.dato = sucesor.dato
        self.der = self.der.BorrarNodo(sucesor.dato)

        return self


# Ejercicio 6
def ImprimirRango(nodo,valor_bajo,valor_alto):

    if nodo is None:
        return None

    if nodo.dato > valor_bajo:
        ImprimirRango(nodo.izq, valor_bajo, valor_alto)
    
    if valor_bajo <= nodo.dato <= valor_alto:
        print(nodo.dato)

    if nodo.dato < valor_alto:
       ImprimirRango(nodo.der, valor_bajo, valor_alto)