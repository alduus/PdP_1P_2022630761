#Castillo Reyes Diego
#Escamilla Reséndiz Aldo
#Lopez Sanchez Adair
#Yañez Martinez Marthon Leobardo
class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.stack:
            return None

        item = self.stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        return item

    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

stack = Stack()

elements = input("Ingresa los elementos de la pila separados por espacios: ").split()
for element in elements:
    stack.push(int(element))

print("El valor mínimo de la pila es:", stack.min())
