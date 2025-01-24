class Grafo:
    def __init__(self):
        """Inicializa un grafo con una lista de vértices y una matriz de adyacencia."""
        self.vertices = []
        self.matriz_adyacencia = []

    def agregar_vertice(self, vertice):
        """
        Agrega un vértice al grafo.
        
        Args:
            vertice: Nombre o identificador del vértice.
        """
        if vertice in self.vertices:
            print(f"El vértice '{vertice}' ya existe.")
            return
        
        self.vertices.append(vertice)
        # Expandir la matriz de adyacencia con ceros
        for fila in self.matriz_adyacencia:
            fila.append(0)
        self.matriz_adyacencia.append([0] * len(self.vertices))
        print(f"Vértice '{vertice}' agregado.")

    def agregar_arista(self, origen, destino, peso=1):
        """
        Agrega una arista entre dos vértices del grafo.
        
        Args:
            origen: Vértice de origen.
            destino: Vértice de destino.
            peso: Peso de la arista. Por defecto es 1.
        """
        if origen not in self.vertices or destino not in self.vertices:
            print("Ambos vértices deben existir en el grafo.")
            return
        
        # Obtener los índices de los vértices
        indice_origen = self.vertices.index(origen)
        indice_destino = self.vertices.index(destino)
        # Establecer el peso en la matriz de adyacencia
        self.matriz_adyacencia[indice_origen][indice_destino] = peso
        print(f"Arista agregada: {origen} -> {destino} con peso {peso}")

    def mostrar_matriz_de_adyacencia(self):
        """Muestra la matriz de adyacencia del grafo."""
        print(" ", " ".join(self.vertices))
        for i, fila in enumerate(self.matriz_adyacencia):
            print(self.vertices[i], " ".join(map(str, fila)))


# Ejemplo de uso
grafo = Grafo()
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_arista("A", "B", 5)
grafo.agregar_arista("B", "C", 3)
grafo.mostrar_matriz_de_adyacencia()