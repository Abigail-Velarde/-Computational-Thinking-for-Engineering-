n= int(input("Dame el tope de la suma: "))
suma= 0
for i in range (1, n+1):
    suma= suma + i
print(f"la suma de 1 hasta {n} es {suma}")

n= int(input("Dame la tabla que quieres: "))
for i in range (1,11):
    multi= n*i
    print(f"{n}x{i}={multi}")
    