from random import randint

def matriz_random(r,c):
    m=[]
    for i in range(r):
        l=[]
        for j in range(c):
            rnd=randint(1,20)
            l.append(rnd)
        m.append(l)
    return m   
    
    
def llena_matriz(r,c):
    matriz=[]
    for i in range(r):
        lista=[]
        for j in range(c):
            dato=int(input("Dame el valor para guardar en la lista: "))
            lista.append(dato)
        matriz.append (lista)   
    return matriz
    
    
def suma_columna(matriz):
    col_a_sumar=int(input("columna a sumar: "))
    suma=0
    for i in range(len(matriz)):
        suma=suma+matriz[i][col_a_sumar]
        print(f)
        
def suma_renglon(matriz):
    sumaren+int(input("renglon a sumar: "))
    suma= sum(matriz[sumaren])
    print(suma)
    
def suma_diagonal(matriz):
    suma=0
    for i in range(len(matriz)):
        suma=suma+matriz[i][i]
        print(matriz[i][i])
    print(suma)

def imprime_valor(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"{matriz[i][j]}",end="   ")
        print()

def main():
    renglon=int(input("Num de renglones: "))
    columna=int(input("Num de datos de cada lista: "))
    matriz_rnd=matriz_random(renglon,columna)
    imprime_valor(matriz_rnd)
    suma_
    
    
main()    