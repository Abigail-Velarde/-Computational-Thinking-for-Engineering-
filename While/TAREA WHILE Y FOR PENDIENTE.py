#Paula Abigail Velarde Rodriguez Matrícula: A01646395
from random import randint

def sumas():
    # Nivel 1: Operaciones con números de un dígito
    contador_correctas = 0
    for i in range(5):
        num1 = randint(1, 9)
        num2 = randint(1, 9)
        respuesta = int(input(f"¿Cuánto es {num1} + {num2}? "))
        if respuesta == (num1 + num2):
            contador_correctas += 1
    
    # Si contestó correctamente las 5 preguntas, avanza a nivel 2
    if contador_correctas == 5:
        print("¡Felicidades! Pasaste al nivel 2.")
        for i in range(5):
            num1 = randint(1, 9)
            num2 = randint(10, 99)
            respuesta = int(input(f"¿Cuánto es {num1} + {num2}? "))
            if respuesta == (num1 + num2):
                contador_correctas += 1
    
        if contador_correctas == 10:
            nombre = input("Escribe tu nombre para el salón de la fama: ")
            print(f"¡Felicidades {nombre}! Has entrado al salón de la fama.")
    else:
        print("No lograste avanzar al nivel 2.")

def resta():
    for i in range(5):
        num1 = randint(10, 99)
        num2 = randint(1, 9)
        #Si no se pone aquí, se cambian los numeros otra vez
        while True:
            respuesta = int(input(f"¿Cuánto es {num1} - {num2}? "))
            if respuesta == (num1 - num2):
                print("¡Correcto!")
                break  # Sale del ciclo cuando la respuesta es correcta
            else:
                print("Incorrecto, intenta de nuevo.")

def multiplicacion():
    contador_correctas = 0
    # 15 operaciones de multiplicación con un dígito
    for i in range(15):
        num1 = randint(1, 9)
        num2 = randint(1, 9)
        respuesta = int(input(f"¿Cuánto es {num1} x {num2}? "))
        if respuesta == (num1 * num2):
            contador_correctas += 1
    print(f"Aciertos: {contador_correctas}/15")


def main():
    while True:
        opcion=int(input("""Menú de Operaciones Aritméticas
    1. Suma
    2. Resta
    3. Multiplicación
    4. Salir
    Elige una opción: """))
        if opcion == 1:
            sumas()  #función de sumas
        elif opcion == 2:
            resta()  #función de restas
        elif opcion == 3:
            multiplicacion()  #función de multiplicación
        elif opcion == 4:
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break  # Sale del ciclo
        else:
            print("Opción inválida, por favor elige nuevamente.")
        
main()
