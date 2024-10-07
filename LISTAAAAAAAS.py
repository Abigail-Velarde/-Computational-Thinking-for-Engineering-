from random import randint 

"""Funcion que genera una lista con numeros consecutivos desde uno"""
def lista_num(n):
    lista=[]
    for i in range(n):
        lista.append(i+1)
    return lista

"""Funcion de numeros consecutivos con rango."""
def lista_rango():
    lista=list(range(1,5))
    return lista

"""Funcion que captura lista con numeros dados por el usuario."""
def lista_usuario(n):
    lista=[]
    for i in range(n):
        dato=int(input(f"Dame el elemento {i+1} de la lista: "))
        lista.append(dato)
    return lista

"""Funcion que captura una lista con numeors random."""
def lista_random(n):
    lista=[]
    for i in range(n):
        dato=randint(1,99)
        lista.append(dato)
    return lista
        
"""Funcion que imprime los elementos de una lista"""
def imprime_lista(lista):
    for valor in lista:
        print(valor, end= " ")
    print()

"""Funcion que imprime los elementos de una listaaa"""
def imprime_lista_indices(lista):
    for i in range(len(lista)):
        print(lista[i], end= " ")
        
def main():
    num=int(input("Dame el numero de datos que quieres en tu lista: "))
    lista01=lista_num(num)
    lista02=lista_usuario(num)
    lista03=lista_random(num)
    lista04=lista_rango()
    print(f"Lista declarada de numeros {lista01}")
    print(f"Lista declarada de numeros {lista02}")
    print(f"Lista declarada de numeros {lista03}")
    print(f"Lista declarada de numeros {lista04}")
    imprime_lista(lista02)
    imprime_lista_indices(lista03)

main()
        