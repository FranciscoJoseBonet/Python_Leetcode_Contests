'''
Design a stack that supports increment operations on its elements.
'''

class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = [0] * maxSize # Creamos una lista para almacenar los datos de nuestra pila
        self.top = -1
        self.incrementStack = [0] * maxSize # Lista auxiliar para incrementos diferidos

    def push(self, x: int) -> None:
        if self.top + 1 < self.maxSize:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1
        else:
            value = self.stack[self.top] + self.incrementStack[self.top] # Aplicamos el incremento diferido antes de hacer pop
            if self.top > 0: # Si no es el último elemento, transferimos el incremento pendiente hacia abajo
                self.incrementStack[self.top - 1] += self.incrementStack[self.top] # Restablecemos el incremento en la posición actual
            self.incrementStack[self.top] = 0
            self.top -= 1
            return value

    def increment(self, k: int, val: int) -> None:
        if self.top >= 0: # Solo registra el incremento diferido en la posición k-1 (el último que debe recibirlo)
            self.incrementStack[min(k - 1, self.top)] += val


'''
Implemente una carga de datos a la salida del pop para no tener que recorrer la lista cada vez que se incrementa, es decir,
solo aplicamos el incremento a la salida del pop
'''