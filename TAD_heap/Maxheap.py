class MaxHeap:
    def __init__(self, elementos = []):
        # Define el heap
        self.elem=[]
        for i in elementos:
            self.elem.append(i)
        self.heapify()

    def heapsize(self):
        # Cantidad de elementos
        return len(self.elem)

    def es_hoja(self, pos):
        # Devuelve True si n es una hoja
        return (pos >= self.heapsize()//2 and pos < self.heapsize())
    
    def hijo_izq(self, pos):
        # Devuelve la posición para el hijo izquierdo de pos
        if pos < self.heapsize()//2:
            return 2*pos + 1
        raise IndexError("La posición no tiene hijo izquierdo")  
      
    def hijo_der(self, pos):
        # Devuelve la posición para el hijo derecho de pos
        if pos < (self.heapsize() - 1)/2:
            return 2*pos + 2
        raise IndexError("La posición no tiene hijo derecho")    
    
    def padre(self, pos):
        # Devuelve la posición del padre de pos
        if pos <= 0:
            raise IndexError("La posición no tiene padre")
        else:
            return (pos-1)//2
        
    def insert(self, val):
        # Inserta un valor en el Heap
        curr = self.heapsize()
        self.elem.append(val)       # Agregamos al final del heap
        # Ahora movemos hacia "arriba" hasta que el padre sea mayor
        while (curr!=0 and (self.elem[curr] > self.elem[self.padre(curr)])):
            self.elem[curr], self.elem[self.padre(curr)] = self.elem[self.padre(curr)], 
            self.elem[curr]
            curr = self.padre(curr)

    def heapify(self):
        # Verifica/transforma a heap un Heap modificado
        n = self.heapsize()//2
        for i in range (n-1, -1, -1):
            self.siftdown(i)

    def siftdown(self, pos):
        # Pone un elemento en su lugar correcto
        n = self.heapsize()
        if pos >= 0 and pos < n :
            while not self.es_hoja(pos):
                j = self.hijo_izq(pos)
                if j<(n-1) and self.elem[j]<self.elem[j+1]:
                    j+=1   # j es el índice del hijo con mayor valor
                if self.elem[pos]>=self.elem[j]:
                    return
                # Intercambiar los elementos
                self.elem[pos], self.elem[j] = self.elem[j], self.elem[pos]
                pos = j  # Mover hacia abajo        
        else:
            raise IndexError("Posición ilegal en el heap")
        
    def removemax(self):
        # Quita y devuelve el valor mayor del heap
        if self.heapsize() <= 0:
            raise IndexError("Heap vacío!")
        else:
            n = self.heapsize()
            # Intercambiar el máximo con el último valor
            self.elem[0], self.elem[n-1] = self.elem[n-1], self.elem[0]
            val = self.elem.pop()
            n -= 1
        print(self.elem)
        if n != 0:              # Si no era el último elemento
            self.siftdown(0)    # Poner el nuevo valor de la raíz en su lugar
        return val
    
    def remove(self, pos):
        # Quita y devuelve el elemento de la posición pos
        n = self.heapsize()
        if pos >=0 and pos < n:
            # Intercambiar el elemento de pos con el último valor
            self.elem[pos], self.elem[n-1] = self.elem[n-1], self.elem[pos]
            val = self.elem.pop()
            while pos > 0 and self.elem[pos] > self.elem[self.padre(pos)]:
                self.intercambiar(pos, self.padre(pos))
                pos = self.padre(pos)
            if n != 0:
                 self.siftdown(pos)  # Empujar hacia abajo
            return val
        else:
            raise IndexError("Posición ilegal en el heap")
    
