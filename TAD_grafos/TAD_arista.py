class Arista:
    def __init__(self, dato=None, peso_arco=0, prox=None):
        self.dato = dato
        self.peso_arco = peso_arco
        self.prox = prox
    def __str__(self):
        return str(self.dato)
    
    def valor(self):
        return self.dato
    
    def proximo(self):
        return self.prox
    
    def peso(self):
        return self.peso_arco
 
    def imprimeLista(nodo):
        """Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos."""
        while nodo:
            print(nodo, end=" "),
            nodo = nodo.prox
        print(" ")
 
    def imprime_lista_con_peso(nodo):
        while nodo:
            print(nodo, "("+str(nodo.peso())+")",end=" "),
            nodo = nodo.prox
        print(" ")