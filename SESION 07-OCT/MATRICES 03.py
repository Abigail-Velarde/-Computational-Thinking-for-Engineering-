from random import randint

"""Funcion para crear una matriz cuadrada de -1"""
def crea_matriz(n):
    matriz=[]
    for i in range(n):
        lista=[]
        for j in range(n):
            dato=-1
            lista.append(dato)
        matriz.append(lista)
    return matriz     
 
"""Funcion para imprimir matriz por valores""" 
def imprime_matriz(matriz):
    for lista in matriz:
        for valor in lista:
            print(valor,end="\t")
        print()    

"""Funcion que contiene los numeros de la columna en que se encuentra cada valor"""
def matriz_columna(n):
    matriz=[]
    for i in range(n):
        lista=[]
        for j in range(n):
            dato=j
            lista.append(dato)
        matriz.append(lista)    
    return matriz

def matriz_renglon(n):
    matriz=[]
    for i in range(n):
        lista=[]
        for j in range(n):
            dato=i
            lista.append(dato)
        matriz.append(lista)    
    return matriz

def matriz_secuencia(n):
    cont=1
    matriz=[]
    for i in range(n):
        lista=[]
        for j in range(n):
            dato= cont
            lista.append(dato)
            cont= cont+1
        matriz.append(lista)
    return matriz

def matriz_random(n):
    m=[]
    for i in range(n):
        l=[]
        for j in range(n):
            rnd=randint(1,20)
            l.append(rnd)
        m.append(l)
    return m   

def matriz_ceros(n):
    m=[]
    for i in range(n):
        l=[]
        for j in range(n):
            rnd=randint(0,3)
            l.append(rnd)
        m.append(l)
    return m   

def cuenta_pares(matriz):
    par=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]%2==0:
                par += 1
    return par

def cuenta_positivos(matriz):
    positivos=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] >= 0:
                positivos += 1
    return positivos  
        
def matriz_secuencia_columna(n):
    matriz=[]
    for i in range(n): 
        lista=[]
        for j in range(n): 
            lista.append(j*n+i)
        matriz.append(lista)
    return matriz

def cambiar_negativos(matriz,n):
    for i in range(n):
        for j in range(n): 
            dato=(matriz[i][j])
            if dato<0:
                dato=0
                matriz[i][j]=dato
            else:
                dato=dato
    return matriz

def cuenta_repeticiones(matriz,x):
    rep=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == x:
                rep += 1
    return rep

def busca(matriz,x):
    cant=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == x:
                cant += 1
    if cant > 0:
        existencia="True"
    else:
        existencia="False"
    return existencia

def suma_mayores5(matriz):
    suma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            dato = matriz[i][j]
            if dato >= 5:
                suma= suma + dato
    return suma

def cambiar_ceros(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])): 
            dato=(matriz[i][j])
            if dato==0:
                matriz[i][j]=i+j
            else:
                dato=dato
    return matriz


def main():
    print("Este programa crea matrices.")
    print()
    num=int(input("Tamano matriz: "))
    ma=crea_matriz(num)
    imprime_matriz(ma)
    ma_random=matriz_random(num)
    print()
    ma_columna=matriz_columna(num)
    imprime_matriz(ma_columna)
    print()
    ma_renglon=matriz_renglon(num)
    imprime_matriz(ma_renglon)
    print()
    ma_sec=matriz_secuencia(num)
    imprime_matriz(ma_sec)
    print()
    ma_sec_col=matriz_secuencia_columna(num)
    imprime_matriz(ma_sec_col)
    print()
    ma_ca_neg=cambiar_negativos(ma_random,num)
    imprime_matriz(ma_ca_neg)
    print()
    ma_c_par=cuenta_pares(ma_random)
    print(ma_c_par)
    ma_c_pos=cuenta_positivos(ma_random)
    print(ma_c_pos)
    num_perdido=int(input("Dame el numero que quieres buscar en tu matriz: "))
    ma_rep=cuenta_repeticiones(ma_random,num_perdido)
    print(ma_rep)
    busqueda=busca(ma_random,num_perdido)
    print(busqueda)
    suma5=suma_mayores5(ma_random)
    print(suma5)
    ma0=matriz_ceros(num)
    imprime_matriz(ma0)
    print()
    c0=cambiar_ceros(ma0)
    imprime_matriz(c0)
    
main()    