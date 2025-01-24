def registrar_usuario():
    """Registra un nuevo usuario solicitando su información."""
    gmail = input("Ingrese su Gmail: ")
    name = input("Ingrese su nombre: ")
    dateofbirth = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
    usuarios_lista.insertalfinalUSUARIO(gmail, name, dateofbirth)
    print(f"Usuario {name} registrado exitosamente.")

def agregar_amigos():
    """Permite agregar amigos a un usuario existente."""
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    nombre_amigo = input("Ingrese el nombre del amigo a agregar: ")
    usuarios_lista.agregar_amigo(nombre_usuario, nombre_amigo)

def buscar_similitudes():
    """
    Encuentra similitudes entre los amigos de los usuarios.
    Imprime usuarios que comparten algún amigo en común.
    """
    current = usuarios_lista.head
    while current:
        amigos = set()
        amigo_actual = current.amigos.head
        while amigo_actual:
            amigos.add(amigo_actual.name)
            amigo_actual = amigo_actual.next
        
        comparador = usuarios_lista.head
        while comparador:
            if comparador.name != current.name:  # Evitar comparar consigo mismo
                amigos_comparador = set()
                amigo_comparador_actual = comparador.amigos.head
                while amigo_comparador_actual:
                    amigos_comparador.add(amigo_comparador_actual.name)
                    amigo_comparador_actual = amigo_comparador_actual.next
                
                comunes = amigos & amigos_comparador
                if comunes:
                    print(f"{current.name} y {comparador.name} tienen amigos en común: {', '.join(comunes)}")
            comparador = comparador.next
        
        current = current.next

def mostrar_usuarios():
    """Muestra todos los usuarios y sus amigos."""
    current = usuarios_lista.head
    while current:
        print(f"Usuario: {current.name}, Gmail: {current.gmail}, Fecha de nacimiento: {current.dateofbirtday}")
        amigos = current.amigos
        amigo_actual = amigos.head
        if amigo_actual:
            print("  Amigos:")
            while amigo_actual:
                print(f"    - {amigo_actual.name} ({amigo_actual.gmail}, {amigo_actual.dateofbirtday})")
                amigo_actual = amigo_actual.next
        else:
            print("  Sin amigos registrados.")
        current = current.next

# Menú del sistema
while True:
    print("\n--- Sistema de Usuarios ---")
    print("1. Registrar nuevo usuario")
    print("2. Agregar amigos")
    print("3. Buscar similitudes entre amigos")
    print("4. Mostrar todos los usuarios")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        agregar_amigos()
    elif opcion == "3":
        buscar_similitudes()
    elif opcion == "4":
        mostrar_usuarios()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, intente de nuevo.")