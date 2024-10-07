"""
Este programa calcula el área del triángulo con base y altura.

INPUT:
medida_base, medida_altura

OUTPUT:
area_triangulo

PROCESS:
1.-Este programa calcula el área del triángulo con base y altura.
2.- Imprimir "Dame la medida de la base de tu triangulo en cm: ", guardarlo en medida_base.
3.-Imprimir "Dame la medida de la altura de tu triangulo en cm: ", guardarlo en medida_altura.
4.- Multiplicar (medida_base * medida altura)/2 y guardarlo en area_triangulo.
5.- Imprimir "El area es: ", imprimir area_triangulo
"""

print("Este programa calcula el área del triángulo con base y altura.")
medida_base= float (input("Dame la medida de la base de tu triangulo en cm: "))
medida_altura= float (input("Dame la medida de la altura de tu triangulo en cm: "))
area_triangulo=(medida_base * medida_altura)/2
print(f"El área es: {area_triangulo:.2f} cm²")