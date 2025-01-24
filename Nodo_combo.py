def insertarL(self,data):
    Nuevonodo = Nodo(data)
    if self.head is None:
        self.head = Nuevonodo
    else:
        actual = self.head
        while actual.next  is not None:
            actual = actual.next
        actual.next = Nuevonodo
        Nuevonodo.prev = actual
        
def mostrar(self):
    nodo_actual = self.head
    while nodo_actual is not None:
            print(nodo_actual.data,end=",")
            nodo_actaul = nodo_actual.next

def buscar(self, dato):
    nodo_actual = self.head
    while nodo_actual is not None:
        if nodo_actual.dato == dato: 
            print("Encontrado")
        else:
            nodo_actual = nodo_actual.next
        print("No encontrado")
