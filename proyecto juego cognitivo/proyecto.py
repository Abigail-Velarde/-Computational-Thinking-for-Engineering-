import random
import time
import os

# Colores disponibles
COLORES = ["Rojo", "Azul", "Verde", "Amarillo", "Morado", "Cian"]

# Longitud inicial del patrón
LONGITUD_PATRON_INICIAL = 4

def limpia():
    '''Función que limpia la pantalla sin importar el sistema operativo'''
    if os.name == 'nt': #Windows
        os.system('cls') 
    else:  #'posix'
        os.system('clear') #Mac/linux

def crear_patron(longitud):
    """Crea un patrón aleatorio de colores"""
    return [random.choice(COLORES) for _ in range(longitud)]

def mostrar_color(color):
    """Muestra un color con su respectivo código ANSI"""
    colores_ansi = {
        "Rojo": "\033[91m",
        "Azul": "\033[94m",
        "Verde": "\033[92m",
        "Amarillo": "\033[93m",
        "Morado": "\033[95m",
        "Cian": "\033[96m"
    }
    return f"{colores_ansi[color]}{color}\033[0m"

def mostrar_patron(patron):
    """Muestra el patrón al jugador"""
    print("Memoriza este patrón:")
    print(" ".join(mostrar_color(color) for color in patron))
    time.sleep(5)  # Espera 5 segundos
    limpia()

def crear_opciones(patron_correcto):
    """Crea opciones para que el jugador elija"""
    opciones = [patron_correcto]
    while len(opciones) < 3:
        opcion_incorrecta = crear_patron(len(patron_correcto))
        if opcion_incorrecta not in opciones:
            opciones.append(opcion_incorrecta)
    random.shuffle(opciones)
    return opciones

def mostrar_opciones(opciones):
    """Muestra las opciones al jugador"""
    for i, opcion in enumerate(opciones, 1):
        print(f"Opción {i}:", " ".join(mostrar_color(color) for color in opcion))

def obtener_respuesta():
    """Obtiene la respuesta del jugador"""
    while True:
        try:
            respuesta = int(input("Elige el número de la opción correcta (1, 2 o 3): "))
            if respuesta in [1, 2, 3]:
                return respuesta
            else:
                print("Por favor, elige 1, 2 o 3.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def mostrar_titulo():
    print("\n" + "=" * 40)
    print("  JUEGO DE RECONOCIMIENTO DE PATRONES  ")
    print("=" * 40 + "\n")

def mostrar_instrucciones():
    print("Instrucciones:")
    print("1. Se te mostrará un patrón de colores.")
    print("2. Memoriza el patrón.")
    print("3. Elige la opción que corresponda al patrón mostrado.")
    print("4. ¡Gana puntos por cada acierto!")
    print("5. La dificultad aumentará cada 3 rondas correctas.\n")

def jugar():
    """Función principal del juego"""
    mostrar_titulo()
    mostrar_instrucciones()
    input("Presiona Enter para comenzar...")
    
    puntuacion = 0
    ronda = 1
    longitud_patron = LONGITUD_PATRON_INICIAL
    
    while True:
        limpia()
        print(f"\nRonda {ronda}")
        patron = crear_patron(longitud_patron)
        mostrar_patron(patron)
        opciones = crear_opciones(patron)
        mostrar_opciones(opciones)
        respuesta = obtener_respuesta()
        
        if opciones[respuesta - 1] == patron:
            print("¡Correcto!")
            puntuacion += 1
            if ronda % 3 == 0:  # Aumentar la longitud cada 3 rondas
                longitud_patron += 1
                print(f"¡La dificultad ha aumentado! Nuevo largo del patrón: {longitud_patron}")
        else:
            print("Incorrecto. El patrón correcto era:", end=" ")
            print(" ".join(mostrar_color(color) for color in patron))
        
        print(f"Tu puntuación actual es: {puntuacion}")
        
        jugar_de_nuevo = input("¿Quieres jugar otra ronda? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            break
        ronda += 1
    
    print(f"\n¡Gracias por jugar! Tu puntuación final es: {puntuacion}")

# Iniciar el juego
if __name__ == "__main__":
    jugar()
