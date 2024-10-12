"""Paula Abigail Velarde Rodriguez A01646395"""
from random import randint

"""Funcion para una matriz con numeros aleatorios."""
def matriz_aleatoria(n):
    matriz=[]
    for i in range(n):
        lista=[]
        for j in range(n):
            dato=randint(1,20)
            lista.append(dato)
        matriz.append(lista)
    return matriz

"""Funcion para imprimir la matriz sin corchetes y mejor acomodada."""
def imprime_lista(m):
    for lista in m:
        for num in lista:
            print(num,end="\t")
            #\t para tabulador
        print()
        
"""Funcion que busca los numeros 10 en la matriz aleatoria."""   
def busca10(matriz):
    diez=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 10:
                diez += 1
    return diez

"""Funcion principal."""
def main():
    num=int(input("Dame el tamano de la matriz:"))
    m_aleatoria=matriz_aleatoria(num)
    imprime_lista(m_aleatoria)
    num10=busca10(m_aleatoria)
    print(f"La matriz cuenta con {num10} numeros 10.")
    
main()   
    