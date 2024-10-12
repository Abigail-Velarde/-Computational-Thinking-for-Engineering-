"""Paula Abigail Velarde Rodriguez A01646395"""

def serie_numero():
    n=int(input("Dame el número para tu serie: "))
    for i in range(n,30,n):
        print(i,end=" ")

def contar_positivos_negativos():
    positivos= 0
    negativos= 0
    cant_num=int(input("¿Cuantos números desea clasificar?"))
    for i in range(cant_num):
        num= int(input("Dame un número:"))
        if num>0:
            positivos= positivos + 1
        else:
            negativos = negativos + 1
    diferencia= positivos - negativos
    print(f"Ha ingresado {positivos} números positivos y {negativos} números negativos.")
    return diferencia         

def main():
    while True:
        opcion=int(input("""¿Qué desea hacer?
            1. Serie de números
            2. Contar números positivos y negativos
            3. Salir
            Opción elegida: """))
        if opcion == 1:
            serie_numero()
        elif opcion == 2:
            diferencia= contar_positivos_negativos()
            print(f"La diferencia entre positivos y negativos es de {diferencia}.")
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

main()