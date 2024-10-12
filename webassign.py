import random
import time
import os

# Colores disponibles
COLORES = ["Rojo", "Azul", "Verde", "Amarillo", "Morado", "Cian"]

# Longitud del patrón
LONGITUD_PATRON = 4

def limpia():
    '''Función que limpia a pantalla sin importar el sistema operativo
      de la máquina donde esté corriendo'''
    if os.name == 'nt': #Windows
        os.system('cls') 
    else:  #'posix'
        os.system('clear') #Mac/linux

def crear_patron():
    """Crea un patrón aleatorio de colores"""
    patron = []
    for i in range(LONGITUD_PATRON):
        color = random.choice(COLORES)
        patron.append(color)
    return patron

def mostrar_patron(patron):
    """Muestra el patrón al jugador"""
    print("Memoriza este patrón:")
    for color in patron:
        if color == "Rojo":
            print("\x1b[0;31m"+color, end=" ")
        elif color == "Azul":
            print("\x1b[0;34m"+color, end=" ")
        elif color == "Verde":
            print("\x1b[0;32m"+color, end=" ")
        elif color == "Amarillo":
            print("\x1b[0;33m"+color, end=" ")
        elif color == "Morado":
            print("\x1b[0;35m"+color, end=" ")
        else:
            print("\x1b[0;36m"+color, end=" ")
    print()
    time.sleep(5)  # Espera 3 segundos
    limpia()
    print("\n" * 100)

def crear_opciones(patron_correcto):
    """Crea opciones para que el jugador elija"""
    opciones = [patron_correcto]
    for _ in range(2):  # Crea dos opciones incorrectas
        opcion_incorrecta = crear_patron()
        while opcion_incorrecta in opciones:
            opcion_incorrecta = crear_patron()
        opciones.append(opcion_incorrecta)
    random.shuffle(opciones)
    return opciones

def mostrar_opciones(opciones):
    """Muestra las opciones al jugador"""
    for i, opcion in enumerate(opciones, 1):
        print(f"Opción {i}:", end=" ")
        for color in opcion:
            if color == "Rojo":
                print("\x1b[0;31m"+color, end=" ")
            elif color == "Azul":
                print("\x1b[0;34m"+color, end=" ")
            elif color == "Verde":
                print("\x1b[0;32m"+color, end=" ")
            elif color == "Amarillo":
                print("\x1b[0;33m"+color, end=" ")
            elif color == "Morado":
                print("\x1b[0;35m"+color, end=" ")
            else:
                print("\x1b[0;36m"+color, end=" ")
        print()

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

def jugar():
    """Función principal del juego"""
    print("¡Bienvenido al Juego de Reconocimiento de Patrones!")
    
    while True:
        patron = crear_patron()
        mostrar_patron(patron)
        opciones = crear_opciones(patron)
        mostrar_opciones(opciones)
        respuesta = obtener_respuesta()
        if opciones[respuesta - 1] == patron:
            print("¡Correcto!")
        else:
            print("Incorrecto. El patrón correcto era:", patron)
        
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            break
    
    print("¡Gracias por jugar!")

# Iniciar el juego
jugar()
