def pares(a,b):
    while a <= b:
        if a%2==0:
            print (a)
        a= a+1
        
    
def main():
    print("Este programa encuentra los numeros pares en el rango entre a y b dados por el usuario, siendo a menor que b.")
    a= int(input("Ingresa el primer numero: "))
    b= int(input("Ingresa el segundo numero: "))
    pares(a,b)
    
main()