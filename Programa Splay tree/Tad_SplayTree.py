class Nodo:
    def __init__(self, dato, frecuencia = 0, padre=None, izq=None, der=None):
        self.dato = dato
        self.izq = izq # Indica el hijo izquierdo
        self.der = der # Indica el hijo derecho
        self.padre = padre # Indica padre o raizo
        
    def __str__(self):
        return str(self.dato)
    
    

class ArbolSplay:
    def __init__(self, raiz = None, cantidad = 0):
        self.raiz = raiz
    

#============================================================================
# OPERACION PUBLICAS (REALIZADAS POR EL USUARIO)

    def Buscar(self,x):
        """ se busca el nodo siguiendo las reglas de un Árbol Binario de Búsqueda. Una 
            vez encontrado, se realiza una operación de biselado (splay) para llevar dicho nodo 
            a la raíz mediante rotaciones, facilitando futuros accesos al mismo. """
        actual = self.raiz
        while actual: 
            if actual.dato == x:
                self.Splay(actual)
                return actual
            elif x < actual.dato:
                actual = actual.izq
            elif x> actual.dato:
                actual = actual.der
        return None 

    def Insertar(self,x):
        """ Se inserta el nuevo nodo siguiendo las reglas de un Árbol Binario de 
            Búsqueda (ABB). Una vez insertado, se realiza una operación de biselado (splay) 
            para llevar el nuevo nodo a la raíz mediante una serie de rotaciones. """
        
        if self.raiz is None: 
            self.raiz = Nodo(x) #Se crea la raíz del árbol
            return self.raiz
        
        #Recorre el árbol buscando la posicion de inserción        
        padre = None
        actual = self.raiz #El que esta en la raíz
        """Voy comparando y bajando el árbol hasta que ya no haya mas comparación"""
        while actual:
            padre = actual #Guarda nodo actual(raiz) antes de seguir bajando
            if x < actual.dato:
                actual = actual.izq
            elif x > actual.dato:
                actual = actual.der
            else:
                #Si el elemento ya existe, lo llevamos a la raíz
                self.Splay(actual)
                return actual

        #Crear el nuevo nodo
        nuevo = Nodo(x,padre)
        if x < padre.dato:
            padre.izq = nuevo
        else:
            padre.der = nuevo
        
        #LLevar el nuevo nodo a la raíz
        self.Splay(nuevo)
        return nuevo
    
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

    def MostrarHistorial (self):
        return
    
#=================================================================================
# OPERACIONES PRIVADAS
    def RotacionIzquierda(self, x):
        y = x.der
        x.der = y.izq
        if y.izq:
            y.izq.padre = x
            
        y.padre = x.padre
        if x.padre is None:
            self.raiz = y
        elif x == x.padre.izq:
            x.padre.izq = y
        else:
            x.padre.der = y
            
        y.izq = x
        x.padre = y
    
    def RotacionDerecha(self, x):
        y = x.izq
        x.izq = y.der
        if y.der:
            y.der.padre = x
        
        y.padre = x.padre
        if x.padre is None:
            self.raiz = y
        elif x == x.padre.der:
            x.padre.der = y
        else:
            x.padre.izq = y
            
        y.der = x
        x.padre = y

    
    def Splay(self, nodo):
        # Sube el nodo hasta que sea raíz
        while nodo.padre is not None:
            # Zig
            if nodo.padre.padre is None:
                if nodo == nodo.padre.izq:
                    self.RotacionDerecha(nodo.padre)
                else:
                    self.RotacionIzquierda(nodo.padre)
            # Zig-Zig
            elif nodo == nodo.padre.izq and nodo.padre == nodo.padre.padre.izq:
                self.RotacionDerecha(nodo.padre.padre)
                self.RotacionDerecha(nodo.padre)
            # Zag-Zag
            elif nodo == nodo.padre.der and nodo.padre == nodo.padre.padre.der:
                self.RotacionIzquierda(nodo.padre.padre)
                self.RotacionIzquierda(nodo.padre)
            # Zig-Zag
            elif nodo == nodo.padre.der and nodo.padre == nodo.padre.padre.izq:
                self.RotacionIzquierda(nodo.padre)
                self.RotacionDerecha(nodo.padre)
            # Zag-Zig
            else:
                self.RotacionDerecha(nodo.padre)
                self.RotacionIzquierda(nodo.padre)
    
    def Minimo(self):
        return

    def Maximo(self):
        return
    
    def UnirSubarboles(self):
        return
    