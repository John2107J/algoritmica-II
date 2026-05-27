class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)
    
    def imprimeLista (self):
        nodo = self
        while nodo:
            print(nodo, end="->")
            nodo = nodo.prox
        print("")
    
    
#Defino una funcion que sea imprimir Nodos
def imprimirNodos(nodo):
    while nodo is not None:
        print(nodo)
        nodo = nodo.prox
    
    
#Como imprimir una lista pero al reves
def imprimirAlReves(nodoi):
    if nodoi== None:
        return
    cabeza = nodoi
    imprimirAlReves(nodoi.prox)
    print(cabeza)


class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.len = 0
    

    def devolver(self, i=None):
        """Elimina el nodo de la posición i, y devuelve el dato contenido."""
        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            #Este else elimina el nodo
            n_ant = self.prim
            n_act = n_ant.prox
            #el for ubica la posicion del nodo a eliminar
            for pos in range(1, i):
                n_ant = n_act #El anterior apunta al actual (nodo a borrar)
                n_act = n_ant.prox #Una vez encontrado el actual, se borra el nodo
            dato = n_act.dato #guarda el dato del nodo a eliminar
            n_ant.prox = n_act.prox #aca cambia el enlace y el anterior del actual apunta al proximo del actual.
        self.len -= 1 
        return dato
    
    def borrar(self, x):
        """Borra la primera aparición del valor x en la lista."""
        if self.len == 0:
            raise ValueError("Lista vacía")
        if self.prim.dato == x:
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox
            if n_act == None:
                raise ValueError("El valor no está en la lista.")
            n_ant.prox = n_act.prox
        self.len -= 1
         
    def insertar(self, i, x):
        """Inserta el elemento x en la posición i."""
        if i < 0 or i > self.len:
            raise IndexError("Posición inválida")
        nuevo = Nodo(x)
        if i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            n_ant = self.prim #apunta al primer nodo
            for pos in range(1, i):
                n_ant = n_ant.prox #Ahora el anterior apunta al nodo anterior de donde quiero ingresar el nuevo nodo
        nuevo.prox = n_ant.prox
        n_ant.prox = nuevo
        self.len +=1

        """EJ: insertar(2,30) en la lista 10->20->40"""
        """else:
            n_ant = self.prim  -> 10
            for pos in range(1, i):
                n_ant = n_ant.prox      recorre la posicion ant = 20 y ant.prox = 40
        nuevo.prox = n_ant.prox  30 -> 40
        n_ant.prox = nuevo  20 -> 30
        self.len +=1"""