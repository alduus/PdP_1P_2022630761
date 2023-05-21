#Castillo Reyes Diego
#Escamilla Reséndiz Aldo
#Lopez Sanchez Adair
#Yañez Martinez Marthon Leobardo
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]


def sort_stack(stack):
    if stack.isEmpty():
        return

    aux_stack = Stack()

    while not stack.isEmpty():
        temp = stack.pop()

        while not aux_stack.isEmpty() and aux_stack.peek() > temp:
            stack.push(aux_stack.pop())

        aux_stack.push(temp)

    #elementos de la pila auxiliar a la pila original
    while not aux_stack.isEmpty():
        stack.push(aux_stack.pop())


stack = Stack()

elements = input("Ingresa los elementos de la pila separados por espacios: ").split()

for element in elements:
    stack.push(int(element))


print("Pila original:")
print(stack.stack)

# Ordenar la pila
sort_stack(stack)


print("Pila ordenada:")
print(stack.stack)