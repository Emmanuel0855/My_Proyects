class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.__titulo = titulo  # Atributo privado
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def obtener_titulo(self):
        return self.__titulo

    def modificar_titulo(self, nuevo_titulo):
        if nuevo_titulo:
            self.__titulo = nuevo_titulo
            print(f"El título ha sido actualizado a: {self.__titulo}")
        else:
            print("El nuevo título no puede estar vacío.")

# Ejemplo de uso
libro = Libro("El Arte de la Guerra", "Sun Tzu", "1772")
print(f"Título original: {libro.obtener_titulo()}")  # Consultar título
libro.modificar_titulo("Tao")  # Modificar título