def imprime_mensaje():
    print("Hola mundo!")

def main():
    print("Este programa imprime un mensaje.")
    veces=int(input("¿Cuantas veces quieres que se imprima el mensaje?"))
    cont=1
    while cont <= veces:
        imprime_mensaje()
        cont= cont + 1
        
main()