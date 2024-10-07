""" Este programa convierte cierta cantidad de monedas a billetes.
INPUT: cantidad
OUTPUT: b200, b50, b20, pesos
Process
1.- Indicar que hace el programa
    Imprimir "Este programa convierte cierta cantidad de monedas a billetes."
2.- Imprimir "Dame la cantidad de monedas de peso: ", guardar en cantidad.
3.- b200= cantidad//200
5.-sobra= cantidad%200
6.- b50=sobra//50
7.- sobra2=sobra%50
8.- b20= sobra2//20
9.-pesos= sobra2%20
10.- Imprimir resultados """

print("Este programa convierte cierta cantidad de monedas a billetes.")
cantidad=int(input("Dame la cantidad de monedas de peso: "))
b200= cantidad//200
sobra= cantidad%200
b50=sobra//50
sobra2=sobra%50
b20= sobra2//20
pesos= sobra2%20
print(f"""{cantidad} monedas de peso equivalen a:
{b200} billetes de 200.00
{b50} billetes de 50.00
{b20} billetes de 20.00
{pesos} monedas de peso""")