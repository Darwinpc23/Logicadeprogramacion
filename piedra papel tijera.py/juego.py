# Función para obtener la elección de un jugador
def obtener_eleccion(jugador):
    """
    Solicita al jugador que elija entre Piedra, Papel o Tijera.
    Valida que la elección sea válida (1, 2 o 3).
    """
    print(f"\n{jugador}, elige tu opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input("Ingresa el número de tu elección: "))
    
    # Estructura repetitiva para asegurar que la entrada sea válida
    while opcion not in [1, 2, 3]:
        print("Opción inválida. Intenta nuevamente.")
        opcion = int(input("Ingresa el número de tu elección: "))
    return opcion
# Función para determinar el ganador

def determinar_ganador(opcion1, opcion2):
    """
    Compara las elecciones de los jugadores según las reglas:
    - Piedra (1) vence a Tijera (3)
    - Papel (2) vence a Piedra (1)
    - Tijera (3) vence a Papel (2)
    Devuelve el resultado del enfrentamiento: "Jugador 1 gana", "Jugador 2 gana" o "Empate".
    """    
    if opcion1 == opcion2:
        return "Empate"
    elif (opcion1 == 1 and opcion2 == 3) or \
         (opcion1 == 2 and opcion2 == 1) or \
         (opcion1 == 3 and opcion2 == 2):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"
