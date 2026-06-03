from TAD_grafos.TAD_Cola import *

def BFS(G, s):
    estado = {}
    padre = {}
    vertices = G.vertices()
    q = Cola()
    
    for ve in vertices:
        if ve != s:
            estado[ve]="N"
            padre[ve] = None
    estado[s] = "D"
    padre[s] = None
    q.encolar(s)
    while not q.esta_vacia():
        u = q.desencolar()
        print(u) #Procesar!!
        adyacente = vertices[u]
        while adyacente:
            valor = adyacente.valor()
            #Procesar arista
            if estado[valor] == "N":
                estado[valor] = "D"
                padre[valor] = u
                q.encolar(valor)
            adyacente = adyacente.proximo()
        estado[u] = "P"
        
