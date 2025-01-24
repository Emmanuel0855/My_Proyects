class Usuario:
    """Clase para representar un nodo en la lista enlazada."""
    def __init__(self, gmail, name, dateofbirthday, amigos):
        self.name = name
        self.gmail = gmail
        self.dateofbirthday = dateofbirthday
        self.amigos = amigos  # Lista de nombres de amigos
        self.next = None

class LinkedListofUSUARIOS:
    """Clase para representar la lista enlazada."""
    def __init__(self):
        self.head = None

    # Método para insertar al final
    def insertar_al_final_usuario(self, gmail, name, dateofbirthday, amigos):
        new_node = Usuario(gmail, name, dateofbirthday, amigos)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Método para registrar usuarios desde la terminal
    def registrar_usuarios(self):
        print("Registro de usuarios:")
        while True:
            # Solicitar datos al cliente
            name = input("Ingrese el nombre del usuario: ")
            gmail = input("Ingrese el correo electrónico: ")
            dateofbirthday = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
            amigos = input("Ingrese los nombres de los amigos separados por comas: ").split(',')

            # Limpiar espacios en los nombres de amigos
            amigos = [amigo.strip() for amigo in amigos]

            # Agregar el usuario a la lista enlazada
            self.insertar_al_final_usuario(gmail, name, dateofbirthday, amigos)

            # Preguntar si desea registrar otro usuario
            continuar = input("¿Desea registrar otro usuario? (s/n): ").lower()
            if continuar != 's':
                break

    # Método para mostrar el registro de usuarios
    def registro_usuarios(self):
        current = self.head
        count = 0
        print("\nRegistro de Usuarios:")
        while current:
            count += 1
            print(f"Usuario {count}:")
            print(f"  Nombre: {current.name}")
            print(f"  Gmail: {current.gmail}")
            print(f"  Fecha de Nacimiento: {current.dateofbirthday}")
            print(f"  Amigos: {', '.join(current.amigos)}")
            current = current.next
        print(f"Total de usuarios registrados: {count}")

# Uso del programa
if __name__ == "__main__":
    usuarios_lista = LinkedListofUSUARIOS()

    # Registrar usuarios desde la terminal
    usuarios_lista.registrar_usuarios()

    # Mostrar registro final
    usuarios_lista.registro_usuarios()