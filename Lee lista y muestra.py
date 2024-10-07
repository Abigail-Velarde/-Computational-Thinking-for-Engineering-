def lista(n):
    lista=[]
    for i in range(n):
        dato=int(input(f"Dame el elemento {i+1} de la lista: "))
        lista.append(dato)
    return lista
        
def imprimir(lista):
   for i in range(len(lista)):
        print(f"lista[{i}]= ", lista[i], end= "\n")

def main():
    while True:
        num=int(input("Dame el numero de elementos en tu lista= "))
        if num > 0:
            lista1=lista(num)
            imprimir(lista1)
            break
        else:
            print("Numero invalido")

main()