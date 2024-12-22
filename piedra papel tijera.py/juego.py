# Programa completo para jugar Piedra, Papel o Tijera
import random
def obtener_eleccion(jugador):
    #Solicita al jugador que elija entre Piedra, Papel o Tijera.
    #Valida que la elección sea válida (1, 2 o 3).
    
    print(f"\n{jugador}, elige tu opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    
    # Solicitar y validar entrada del jugador
    try:
        opcion = int(input("Ingresa el número de tu elección (o se asignará aleatoriamente): "))
    except (ValueError, OSError):
        print("Entrada no válida o no disponible. Se asignará una opción aleatoria.")
        from random import choice
        opcion = choice([1, 2, 3])
        print(f"Opcion asignada: {opcion}")
    
    while opcion not in [1, 2, 3]:
        print("Opción inválida. Intenta nuevamente.")
        try:
            opcion = int(input("Ingresa el número de tu elección: "))
        except (ValueError, OSError):
            print("Entrada no válida o no disponible. Se asignará una opción aleatoria.")
            opcion = choice([1, 2, 3])
            print(f"Opcion asignada: {opcion}")
    
    return opcion

def determinar_ganador(opcion1, opcion2):
    
   # Compara las elecciones de los jugadores según las reglas:
   # - Piedra (1) vence a Tijera (3)
   # - Papel (2) vence a Piedra (1)
  #  - Tijera (3) vence a Papel (2)
   # Devuelve el resultado del enfrentamiento: "Jugador 1 gana", "Jugador 2 gana" o "Empate".
    
    if opcion1 == opcion2:
        return "Empate"
    elif (opcion1 == 1 and opcion2 == 3) or \
         (opcion1 == 2 and opcion2 == 1) or \
         (opcion1 == 3 and opcion2 == 2):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"

def jugar_piedra_papel_tijera():
    
   # Función principal para gestionar el flujo del juego entre dos jugadores.
    
    print("Bienvenidos al juego de Piedra, Papel o Tijera!")
    
    jugar_de_nuevo = True
    while jugar_de_nuevo:
        # Obtener elecciones de los jugadores
        eleccion_jugador1 = obtener_eleccion("Jugador 1")
        eleccion_jugador2 = obtener_eleccion("Jugador 2")
        
        # Determinar el ganador
        resultado = determinar_ganador(eleccion_jugador1, eleccion_jugador2)
        
        # Mostrar resultados
        opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
        print(f"\nJugador 1 eligió: {opciones[eleccion_jugador1]}")
        print(f"Jugador 2 eligió: {opciones[eleccion_jugador2]}")
        print(f"\nResultado: {resultado}")
        
        # Preguntar si desean volver a jugar
        respuesta = input("\n¿Desean jugar de nuevo? (s/n): ").strip().lower()
        if respuesta != 's':
            jugar_de_nuevo = False

# Ejecutar el juego
if __name__ == "__main__":
    jugar_piedra_papel_tijera()
