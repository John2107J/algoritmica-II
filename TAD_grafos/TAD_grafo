from TAD_listaenlazada import Nodo

class Grafo:
    def __init__(self, es_dirigido = False):
        self.lista_vertices = {}
        self.n_arcos = 0
        self.es_dirigido = es_dirigido

    def __str__(self):
        return "G = ("+str(self.n_vertices())+" V, "+str(self.n_arcos)+" A)"

    def n_vertices(self):
        return len(self.lista_vertices)

    def dirigido(self):
        return self.es_dirigido

    def vertices(self):
        return self.lista_vertices

    def n_arcos(self):
        return self.n_arcos

    def insertar(self, x, z, dirigido = False):
        """ Agregar el vértice de origen """
        if x not in self.lista_vertices:
            self.lista_vertices[x]= None
        """ Agregar el destino (ojo, x sumideros)"""
        
        if z not in self.lista_vertices:
            self.lista_vertices[z]= None

        nw = Nodo(z, self.lista_vertices[x])
        self.lista_vertices[x] = nw
        self.n_arcos+=1
        if dirigido is False and z != x:
            self.insertar(z,x, True)

    def imprimir(self):
        for vertice in self.lista_vertices:
            print(vertice, end=' ')
            arco = self.lista_vertices[vertice]
            if arco is not None:
                print("->", end=' ')
                arco.imprimeLista()
            else:
                print("")

def cargargrafo (gch):
    gch.insertar ("Esquel","Tecka")
    gch.insertar ("Tecka","Rio Pico")
    gch.insertar ("Tecka","Trelew")
    gch.insertar ("Tecka","Sarmiento")
    gch.insertar ("Sarmiento","Comodoro Rivadavia")
    gch.insertar ("Trelew","Puerto Madryn")
    gch.insertar ("Trelew","Rawson")
    gch.insertar ("Trelew","Comodoro Rivadavia")
    gch.insertar ("Rawson","Playa Union")

migrafo = Grafo()
cargargrafo(migrafo)
migrafo.imprimir()
