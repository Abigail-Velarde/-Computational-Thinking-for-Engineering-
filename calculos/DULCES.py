"""Este programa calcula la cantidad de productos que un cliente puede canjear al usar su tarjeta de regalo.
INPUT:
valor_tarjeta
OUTPUT:
chocolates, paletas, chicles
Process
1 Imprimir "Este programa calcula la cantidad de productos que un cliente puede canjear al usar su tarjeta de regalo."
2 Imprimir ""Por favor ingrese el valor de la tarjeta de regalo: ", guardar en valor_tarjeta.
3 chocolates = cantidad//20
4 residuo= valor_tarjeta%20
5 paletas=residuo//5
6 chicles=residuo%5
7 Imprimir resultados"""

print("Este programa calcula la cantidad de productos que un cliente puede canjear al usar su tarjeta de regalo.")
valor_tarjeta=int(input("Por favor ingrese el valor de la tarjeta de regalo en pesos: "))
chocolates = valor_tarjeta//20
residuo= valor_tarjeta%20
paletas=residuo//5
chicles=residuo%5
print(f"""${valor_tarjeta: .2f} equivalen a:
{chocolates} chocolates
{paletas} paletas de chile
{chicles} chicles""")