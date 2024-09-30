'''
MYCIRCULARDEQUEUE

'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.frente = None
        self.final = None
        self.count = 0

    def isEmpty(self) -> bool:
        return self.frente == None and self.final == None
      
    def insertFront(self, value: int) -> bool:
        if self.count == self.size:
            return False
        
        nuevo_nodo = Nodo(value)
        if self.isEmpty():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.frente
            self.frente.anterior = nuevo_nodo
            self.frente = nuevo_nodo
        
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.count == self.size:
            return False
        
        nuevo_nodo = Nodo(value)
        if self.isEmpty():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.final
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        if self.frente == self.final:
            self.frente = self.final = None
        else:
            self.frente = self.frente.siguiente
            self.frente.anterior = None
        
        self.count -= 1  # Corregido: Disminuir el contador
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.frente == self.final:  # Si solo hay un nodo
            self.frente = self.final = None
        else:
            self.final = self.final.anterior
            self.final.siguiente = None
        
        self.count -= 1  # Corregido: Disminuir el contador
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.frente.valor

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.final.valor

    def isFull(self) -> bool:
        return self.size == self.count