class Pila:
    def __init__(self):
        self.elementos=[]

    def apilar(self,elem):
        self.elementos.append(elem)

    def desapilar(self):
        return self.elementos.pop()
    
    def EsVacia(self):
        return (self.elementos ==[])
    
    def __str__ (self):
        return str(self.items)
    
    