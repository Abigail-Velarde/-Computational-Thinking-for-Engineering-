def perfecto(n):
    cont=1
    d=0
    while cont<n:
        if n % cont== 0:
            d=d+cont
            cont=cont+1
        else:
            cont=cont+1
        
    if d==n:
        print("Es perfecto")
    else:
        print("No es perfecto")
        
def main():
    n=int(input("NUMERO: "))
    perfecto(n)
    
main()