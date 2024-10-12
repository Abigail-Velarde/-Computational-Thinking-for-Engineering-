"""
Este programa calcula el cambio de pesos a dólares.
INPUT:
cantidad_pesos, pesos_p_dolar
OUTPUT:
dolares
PROCESS:
1.-Este programa calcula el cambio de pesos a dólares.
2.- Imprimir "Dame la cantidad de pesos que deseas convertir: ", guardarlo en cantidad_pesos.
3.-Imprimir "Dame el costo del dólar actual: ", guardarlo en pesos_p_dolar.
4.- Dividir cantidad_pesos entre pesos_p_dolar y guardarlo en dolares
5.- Imprimir "Usted tiene: ", imprimir dolares, imprimir " dólares."
"""

print("Este programa calcula el cambio de pesos a dólares.")
cantidad_pesos= float (input("Dame la cantidad de pesos que deseas convertir: "))
pesos_p_dolar= float (input("Dame el costo del dólar actual: "))
dolares= cantidad_pesos / pesos_p_dolar
print(f"Usted tiene: ${dolares:.2f}")