par=0
impar=0
for i in range (10):
    n=int(input("Dame un numero: "))
    if n%2==0:
        par= par+1
    else:
        impar= impar+1
print(f"Hay {par} números pares y {impar} números impares.")

