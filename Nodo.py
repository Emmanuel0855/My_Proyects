class Nodo:
    def __init__(self, data):
        self.dato = data # datos del nodo
        self.next = None  # puntero siguiente
 
class LinkedList:
    def __init__(self):
        self.head = None   # inicializar la cabeza con None
 
    def inserta(self, dato):
        nuevonodo = Nodo(dato)
        if self.head != None:
            nuevonodo.next = self.head
            self.head = nuevonodo
        else:
            self.head = nuevonodo
    def imprime(self):
        nodo = self.head
        while nodo != None:
            print(nodo.dato)
            nodo = nodo.next

a = LinkedList()
a.inserta("Hola")
a.inserta(123)
a.imprime()

b = LinkedList()
b.inserta(12)
b.inserta(13)
b.inserta(14)