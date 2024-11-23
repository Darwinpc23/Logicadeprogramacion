def obtener_eleccion(jugador):
    print(f"\n{jugador}, elige tu opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input("Ingresa el número de tu elección: "))
    while opcion not in [1, 2, 3]:
        print("Opción inválida. Intenta nuevamente.")
        opcion = int(input("Ingresa el número de tu elección: "))
    return opcion
