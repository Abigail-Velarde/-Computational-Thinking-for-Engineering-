"""
Este programa calcula el año en que una persona cumplirá 100 años.

INPUT:
edad, a_actual

OUTPUT:
centenario

PROCESS:
1.-Este programa calcula el promedio de 4 materias
2.- Imprimir "Dame tu edad: ", guardarlo en edad.
3.- Imprimir "Dame el año actual: ", guardarlo en a_actual.
6.- Restar edad a a_actual, sumar 100, guardar en centenario.
8.- El año en que cumplirá 100 años es: ", imprimir centenario.

"""

print("Este programa calcula el año que una persona cumplirá 100 anos")
edad= int (input("Dame la edad: "))
a_actual= int (input("Dame el año actual: "))
centenario= (a_actual - edad) + 100
print(f"El año en que cumplirá 100 años es: {centenario}")