class Stack:
    def _init_(self):
        self.elementos = []
    
    def push(self,elemento):
        self.elementos.append(elemento)
    def pop(self):
        return self.elementos.pop()
    def peek(self):
        return self.elementos[len(self.elementos)-1]
    def size(self):
        return len(self.elementos)
    def is_empty(self):
        return len(self.elementos) == 0
    
a = Stack()
a.push(1)
a.push("hola")
a.push(34)
print(a.peek())
a.pop()
print(a.peek())