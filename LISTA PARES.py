def lista_num(lista,dato):
    lista.append(dato)
    return lista
        
def imprimir(lista):
   print

def main():
    while True:
        num=int(input("Dame el numero que quieres: "))
        lista=[]
        if num >= 0:
            lista1=lista_num(lista,num)
        else:
            imprimir(lista1)

main()