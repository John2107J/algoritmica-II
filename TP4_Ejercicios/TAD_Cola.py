class Cola:
    def __init__(self):
        self.elementos=[]

    def encolar(self,elem):
        self.elementos.append(elem)

    def desencolar(self):
        if self.EsVacia():
            raise IndexError("La cola esta vacia ")
        return self.elementos.pop(0)
    
    def EsVacia(self):
        return len(self.items) == 0
        
    def __str__ (self):
        return str(self.items)