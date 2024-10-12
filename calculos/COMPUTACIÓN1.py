"""
Este programa calcula el total a pagar por la compra de una bolsa de naranjas.
INPUT:
precio_kilo, peso
OUTPUT:
costo
PROCESS:
1.- Indicar que hace el programa.
2.- Imprimir "Dame el precio por kilo de naranjas", guardarlo en precio_kilo.
3.- Imprimir "Dime cuánto pesa tu bolsa de naranjas en kilos", guardarlo en peso.
4.- Multiplicar precio_kilo por peso, guardarlo en la variable costo.
5.- Imprimir "El pago total será ", imprimir la variable costo.
6.- Fin del programa
"""

print("Este programa calcula el total a pagar por la compra de una bolsa de naranjas.")
precio_kilo= float (input("Dame el precio por kilo de naranjas: "))
peso= float (input("Dime cuánto pesa tu bolsa de naranjas en kilos: "))
costo= precio_kilo * peso
print(f"El pago total será ${costo:.2f}")