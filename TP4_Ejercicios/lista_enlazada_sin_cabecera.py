class ListaSimple:
    def __init__ (self):
        self.cabeza = None
        self.len = 0

class Nodo:
    def __init__(self, dato,prox):
        self.dato = dato
        self.prox = prox
    
    def __str__ (self):
        return str (self.dato)

cabeza = ListaSimple ()
n1 = Nodo ("lechuga", None)
n2 = Nodo ("tomate", None)
n3 = Nodo ("limon", None)

n1.prox = n2
n2.prox = n3

def imprimir_nodos (nodo):
    while nodo is not None:
        print (nodo)
        nodo = nodo.prox

def imprimir_al_revez (nodoi):
    if nodoi == None:
        return
    imprimir_al_revez (nodoi.prox)

    cabeza = nodoi 
    imprimir_al_revez (nodoi.prox)
    print (cabeza)

imprimir_nodos (n1)
imprimir_al_revez (n1)