from TAD_grafos import *
from TAD_Cola import *

def procesar_vertice_temprano(valor_vertice):
    print("Vértice ", valor_vertice)

def procesar_vertice_tarde(valor_vertice):
    return None

def procesar_arista(valx, valy):
    print("    Arista({},{})".format(valx, valy))

def BFS(G, s):
    estado = {}     # Estado de Vértices
    padre = {}      # Nodos con sus padres
    vertices = G.vertices()
    q = Cola()
                    # Seteo inicial de V
    for ve in vertices:
        if ve != s:
            estado[ve]="N"
            padre[ve] = None
                    # Analizar V inicial
    estado[s] = "D"
    padre[s] = None
    q.encolar(s)
    
    """ Mientras haya vértices que procesar """
    while not q.esta_vacia():
        u = q.desencolar()
        
        procesar_vertice_temprano(u)
        estado[u] = "P"
        adyacente = vertices[u]
        
        while adyacente:        # Descubrir adyacentes!
            valor = adyacente.valor()
            if estado[valor] != "P" or G.dirigido():
                procesar_arista(u, valor)
            if estado[valor] == "N":
                q.encolar(valor)
                estado[valor] = "D"
                padre[valor] = u
                
            adyacente = adyacente.proximo()
        procesar_vertice_tarde(u)

    """ Devolver el diccionario de vertices con sus padres!!
        Para armar el árbol resultante """
    return padre
