L_Ops = ['/','*','+','-']
class ArbolBE:
    def __init__(self, dato, izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der

    def izquierdo(self, dato):
        self.izq = ArbolBE(dato)

    def derecho(self, dato):
        self.der = ArbolBE(dato)
        
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
    
    # Ejercicio 7
    def Evaluar(self):
        # Caso base: nodo hoja (operando)
        if self.dato not in L_Ops:
            return float(self.dato)

        # Evaluo ambos subarboles y aplico el operador
        izq_val = self.izq.Evaluar()
        der_val = self.der.Evaluar()

        if self.dato == '+':
            return izq_val + der_val
        elif self.dato == '-':
            return izq_val - der_val
        elif self.dato == '*':
            return izq_val * der_val
        elif self.dato == '/':
            # Previene en caso de dividir po 0
            if der_val == 0:
                raise ZeroDivisionError("Division por cero en la expresion")
            return izq_val / der_val
        
    
