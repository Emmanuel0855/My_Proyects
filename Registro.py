class LinkedListofUSUARIOS:
    # Resto de la clase...

    def imprimir_registro(self):
        """
        Muestra la cantidad de usuarios registrados y la información de cada uno.
        """
        current = self.head
        contador = 0
        print("Registro de Usuarios:\n")
        while current:
            contador += 1
            print(f"Usuario {contador}:")
            print(f"  Gmail: {current.gmail}")
            print(f"  Nombre: {current.name}")
            print(f"  Fecha de Nacimiento: {current.dateofbirtday}")
            if current.amigos.head:
                print("  Amigos:")
                amigos_actual = current.amigos.head
                while amigos_actual:
                    print(f"    - {amigos_actual.name} ({amigos_actual.gmail})")
                    amigos_actual = amigos_actual.next
            else:
                print("  Amigos: No tiene amigos registrados.")
            print("-" * 40)
            current = current.next
        print(f"Total de usuarios registrados: {contador}")

usuarios = LinkedListofUSUARIOS()
usuarios.insertalfinalUSUARIO("usuario1@gmail.com", "Usuario Uno", "2000-01-01")
usuarios.insertalfinalUSUARIO("usuario2@gmail.com", "Usuario Dos", "1999-02-02")
usuarios.agregar_amigo("Usuario Uno", "Usuario Dos")

usuarios.imprimir_registro()