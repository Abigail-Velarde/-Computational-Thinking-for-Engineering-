""""Manipular una tabla de datos para obtener informacion"""

def inicializa_matriz():
    matriz=[
        ["01","Sonia Garay",10, 60000],
        ["02","Miriam Garza",5,23000],
        ["03","Erika Crespo",5,18000],
        ["04","Mercedes Ozuna",12,45000]
        ]
    return matriz

def imprime_matriz(matriz):
    print()
    print("IDENTIFICADOR\tNombre Del Empleado\tAntiguedad\tSUELDO")
    for lista in matriz:
        print("\t")
        for valor in lista:
            print(valor,end="\t\t")
        print()

def aumenta_sueldo(matriz):
    for i in range(len(matriz)):
        if matriz[i][2]>=10:
            matriz[i][3]=round(matriz[i][3]*1.1)
    return matriz        

def main():
    m=inicializa_matriz()
    imprime_matriz(m)
    aumenta_sueldo(m)
    m_aumento=aumenta_sueldo(m)
    imprime_matriz(m_aumento)
    
main()    