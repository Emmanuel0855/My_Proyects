from collections import deque

class Usuario:
    """Clase para representar un nodo en la lista enlazada de usuarios."""
    def __init__(self, gmail, name, dateofbirth):
        self.gmail = gmail
        self.name = name
        self.dateofbirth = dateofbirth
        self.amigos = LinkedListofUSUARIOS()  # Lista enlazada de amigos
        self.next = None  # Siguiente nodo en la lista principal


class LinkedListofUSUARIOS:
    """Clase para representar la lista enlazada principal."""
    def __init__(self):
        self.head = None

    def insertalfinalUSUARIO(self, gmail, name, dateofbirth):
        new_node = Usuario(gmail, name, dateofbirth)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search_by_gmail(self, gmail):
        """Busca un usuario por correo electrónico."""
        current = self.head
        while current:
            if current.gmail == gmail:
                return current
            current = current.next
        return None

    def search_by_name(self, name):
        """Busca un usuario por nombre."""
        current = self.head
        while current:
            if current.name == name:
                return current
            current = current.next
        return None

    def agregar_amigo(self, nombre_usuario, nombre_amigo):
        """
        Agrega un amigo a un usuario existente en la lista principal.
        """
        # Buscar usuario principal
        usuario = self.search_by_name(nombre_usuario)
        if not usuario:
            print(f"El usuario '{nombre_usuario}' no existe en la lista principal.")
            return

        # Buscar al amigo en la lista principal
        amigo = self.search_by_name(nombre_amigo)
        if not amigo:
            print(f"El usuario '{nombre_amigo}' no existe en la lista principal.")
            return

        # Verificar si el amigo ya está en la lista de amigos
        if usuario.amigos.search_by_name(amigo.name):
            print(f"{amigo.name} ya es amigo de {usuario.name}.")
        else:
            usuario.amigos.insertalfinalUSUARIO(amigo.gmail, amigo.name, amigo.dateofbirth)
            amigo.amigos.insertalfinalUSUARIO(usuario.gmail, usuario.name, usuario.dateofbirth)  # Mutual friendship
            print(f"{amigo.name} agregado como amigo de {usuario.name}.")

    def recomendar_amigos(self, nombre_usuario):
        """
        Recomienda amigos a un usuario específico utilizando el algoritmo de búsqueda en anchura (BFS).
        """
        # Buscar usuario principal
        usuario = self.search_by_name(nombre_usuario)
        if not usuario:
            print(f"El usuario '{nombre_usuario}' no existe en la lista principal.")
            return []

        # Crear una cola para BFS
        cola = deque([usuario])

        # Crear un conjunto para almacenar amigos recomendados
        amigos_recomendados = set()

        # Crear un conjunto para almacenar amigos directos del usuario
        amigos_directos = set()

        # Agregar amigos directos del usuario al conjunto
        current_amigo = usuario.amigos.head
        while current_amigo:
            amigos_directos.add(current_amigo.name)
            current_amigo = current_amigo.next

        # Realizar BFS
        visitados = set([usuario.name])
        while cola:
            actual_usuario = cola.popleft()

            # Agregar amigos del usuario actual a la cola
            current_amigo = actual_usuario.amigos.head
            while current_amigo:
                amigo_obj = self.search_by_name(current_amigo.name)  # Obtener el objeto Usuario
                if amigo_obj and amigo_obj.name not in visitados:
                    visitados.add(amigo_obj.name)
                    if amigo_obj.name not in amigos_directos and amigo_obj.name != usuario.name:
                        amigos_recomendados.add(amigo_obj.name)
                    cola.append(amigo_obj)
                current_amigo = current_amigo.next

        return list(amigos_recomendados)


# Crear la lista principal de usuarios
usuarios_lista = LinkedListofUSUARIOS()


def crear_o_iniciar_sesion():
    """Crea una cuenta o permite iniciar sesión."""
    gmail = input("Ingrese su Gmail: ")
    usuario = usuarios_lista.search_by_gmail(gmail)
    if usuario:
        print(f"Inicio de sesión exitoso. Bienvenido, {usuario.name}.")
        return usuario
    else:
        print("El correo no está registrado. Procederemos a registrar una nueva cuenta.")
        name = input("Ingrese su nombre: ")
        dateofbirth = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        usuarios_lista.insertalfinalUSUARIO(gmail, name, dateofbirth)
        print(f"Usuario {name} registrado exitosamente.")
        return usuarios_lista.search_by_gmail(gmail)


def registrar_amigos(usuario):
    """Permite registrar amigos para un usuario."""
    while True:
        nombre_amigo = input("Ingrese el nombre del amigo a registrar (o 'salir' para terminar): ")
        if nombre_amigo.lower() == "salir":
            break
        usuarios_lista.agregar_amigo(usuario.name, nombre_amigo)


def mostrar_amigos(usuario):
    """Muestra la lista de amigos de un usuario."""
    if usuario.amigos.head is None:
        print(f"{usuario.name} no tiene amigos registrados.")
        return

    print(f"Amigos de {usuario.name}:")
    current_amigo = usuario.amigos.head
    while current_amigo:
        print(f"  - {current_amigo.name} ({current_amigo.gmail}, {current_amigo.dateofbirth})")
        current_amigo = current_amigo.next


def recomendar_amigos(usuario):
    """Muestra amigos recomendados para el usuario actual."""
    recomendaciones = usuarios_lista.recomendar_amigos(usuario.name)
    if recomendaciones:
        print(f"Amigos recomendados para {usuario.name}: {', '.join(recomendaciones)}")
    else:
        print(f"No hay amigos recomendados para {usuario.name}.")


# Menú principal
usuario_actual = None
while True:
    if not usuario_actual:
        print("\n--- Sistema de Gestión de Usuarios ---")
        print("1. Crear cuenta o iniciar sesión")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario_actual = crear_o_iniciar_sesion()
        elif opcion == "2":
            print("¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
    else:
        print("\n--- Bienvenido al sistema ---")
        print("1. Registrar amigos")
        print("2. Mostrar amigos")
        print("3. Recomendar amigos")
        print("4. Cerrar sesión")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_amigos(usuario_actual)
        elif opcion == "2":
            mostrar_amigos(usuario_actual)
        elif opcion == "3":
            recomendar_amigos(usuario_actual)
        elif opcion == "4":
            print("Cerrando sesión...")
            usuario_actual = None
        elif opcion == "5":
            print("¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")