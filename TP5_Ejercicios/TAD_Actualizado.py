class Nodo:
    def __init__(self,dato,prox = None):
        self.dato = dato
        self.prox = prox
        
    def __str__(self):
        return str(self.dato)
    
    
#Defino una funcion que sea imprimir Nodos
def imprimirNodos(nodo):
    while nodo is not None:
        print(nodo)
        nodo = nodo.prox


#Como imprimir una lista pero al reves
def imprimirAlReves(nodoi):
    if nodoi is None:
        return
    cabeza = nodoi
    imprimirAlReves(nodoi.prox)
    print(cabeza)


class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.ult_nodo= None

    def __str__(self):
        n = self.prim
        cadena = ""
        while n is not None:
            cadena += str(n.dato) + "->"
            n = n.prox
        return cadena + "None"
    
    def __len__(self):
        n = self.prim
        contador = 0
        #Mientras exista un nodo, suma 1 y avanza al siguiente hasta saber cuantos nodos tiene la lista
        while n is not None: 
            contador += 1
            n = n.prox
        return contador
    

    def devolver(self, i=None):
        """Elimina el nodo de la posición i, y devuelve el dato contenido."""
        if i is None:
            i = len(self) - 1

        if i < 0 or i >= len(self):
            raise IndexError("Índice fuera de rango")
        
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
            
            if self.prim is None:
                self.ult_nodo = None
            return dato
        
        n_ant = self.prim 
        n_act = n_ant.prox #Se va enlazando cada uno de los nodos
        for pos in range(1, i):
            n_ant = n_act #El anterior va a apuntar al nodo actual(el nodo a borrar)
            n_act = n_ant.prox #Una vez encontrado el nodo actual, se borra el nodo
        dato = n_act.dato #Guarda el dato donde borre el nodo
        n_ant.prox = n_act.prox #Cambia el enlace, el ant.prox apunta al proximo nodo que borre
        
        if n_act == self.ult_nodo:
            self.ult_nodo = n_ant

        return dato
    
    def borrar(self, x):
        """Borra la primera aparición del valor x en la lista."""
        if self.prim is None:
            raise ValueError("Lista vacía")
        
        #Borrar el primero
        if self.prim.dato == x: 
            self.prim = self.prim.prox 
            
            #Si quedo vacía
            if self.prim is None:
                self.ult_nodo = None
            return
        
        n_ant = self.prim
        n_act = n_ant.prox

        while n_act is not None and n_act.dato != x:
            n_ant = n_act
            n_act = n_ant.prox

        if n_act == None:
            raise ValueError("El valor no está en la lista.")
        
        
        n_ant.prox = n_act.prox

        #Si borre el ultimo
        if n_act == self.ult_nodo:
            self.ult_nodo = n_ant

    def insertar(self, i, x):
        """Inserta el elemento x en la posición i."""
        if i < 0 or i > len(self):
            raise IndexError("Posición inválida")
        
        nuevo = Nodo(x)

        if i == 0:
            nuevo.prox = self.prim  
            self.prim = nuevo
            #Si era el primero y único
            if self.ult_nodo is None:
                self.ult_nodo = nuevo
        else:
        
            n_ant = self.prim 
            for pos in range(1, i):
                n_ant = n_ant.prox 
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo

        #Si inserte al final
        if nuevo.prox is None:
            self.ult_nodo = nuevo
         
    
    def agregar(self, x):
        """Agregar al final"""
        nuevoNodo = Nodo(x)

        if self.prim is None:
            self.prim = nuevoNodo
            self.ult_nodo = nuevoNodo
        else:
            self.ult_nodo.prox = nuevoNodo
            self.ult_nodo = nuevoNodo

    
    def indice(self, x):
        n = self.prim
        indice = 0
        while n is not None:
            if n.dato == x:
                return indice  
            n = n.prox
            indice += 1
        return -1 
    
    def imprimeLista (self):
        nodo = self
        while nodo:
            print(nodo, end="->")
            nodo = nodo
            return
        print("")
    
    def iguales(self,otra):
        L1 = self.prim
        L2 = otra.prim

        if len(self) != len(otra):
            return False
        
        while L1 is not None and L2 is not None:

            if L1.dato != L2.dato:
                return False
        
            L1 = L1.prox
            L2 = L2.prox

        return True
    
    def intercambiar(self, x):
        actual = self.prim
        prev = None       # nodo justo antes de 'actual'
        prev_prev = None  # nodo dos posiciones antes de 'actual'

        while actual is not None:

            if actual.dato == x:

                # Si no hay anterior, no hay con quién intercambiar
                if prev is None:
                    return

                # --- Intercambio de 'prev' con 'actual' ---
                # 1. El nodo dos posiciones atrás ahora apunta a 'actual'
                if prev_prev is None:
                    self.prim = actual
                else:
                    prev_prev.prox = actual

                # 2. 'prev' apunta a lo que seguía a 'actual'
                prev.prox = actual.prox

                # 3. 'actual' apunta a 'prev'
                actual.prox = prev

                return

            # Avanzar los tres punteros
            prev_prev = prev
            prev = actual
            actual = actual.prox
    

    def mezclarListas(self, otra):

        l3 = []

        # Recorrer primera lista
        actual = self.prim
        while actual is not None:
            l3.append(actual.dato)
            actual = actual.prox

        # Recorrer segunda lista
        actual = otra.prim
        while actual is not None:
            l3.append(actual.dato)
            actual = actual.prox

        # Ordenar de mayor a menor
        l3 = sorted(l3, reverse=True)

        return l3

