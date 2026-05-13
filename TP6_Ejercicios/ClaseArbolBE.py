L_Ops = ['/','*','+','-']
class Arbol:
    def __init__(self, dato, izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der

    def izquierdo(self, dato):
        self.izq = Arbol(dato)

    def derecho(self, dato):
        self.der = Arbol(dato)
        
    def __str__(self):
        return str(self.dato)

    def printInfijo(self):
        if self.izq is not None:
            self.izq.printInfijo()
        print(self, end= " ")   
        if self.der is not None:
            self.der.printInfijo()

    def printPrefijo(self):
        print(self, end= " ")   
        if self.izq is not None:
            self.izq.printPrefijo()
        if self.der is not None:
            self.der.printPrefijo()
        
    def printPosfijo(self):
        if self.izq is not None:
            self.izq.printPosfijo()
        if self.der is not None:
            self.der.printPosfijo()
        print(self, end= " ")

    def printInfijoCP(self):
        if self.dato in L_Ops:
            print('(', end= "")
        if self.izq is not None:
            self.izq.printInfijoCP()
        print(self, end= "")   
        if self.der is not None:
            self.der.printInfijoCP()
        if self.dato in L_Ops:
            print(')', end= "")
        
    
