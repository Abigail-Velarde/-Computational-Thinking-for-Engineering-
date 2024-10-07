def suma_entero(tope):
    cont=1
    suma=0
    while cont <= tope:
        suma = suma+cont
        cont= cont + 1
        print(f"La suma de 1 hasta {tope} es {suma}")

def main():
    print("Este programa...")
    num= int(input("¿Hasta que numero deseas la suma?"))
    suma_entero(num)

main()