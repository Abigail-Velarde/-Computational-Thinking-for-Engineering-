"""
Este programa pide al usuario los valores a, b y c y calcule y muestre el área del triángulo 
INPUT
lado_a,lado_b,lado_c

OUTPUT
area_tri

"""

import math
up="\u00B2"
print("Este programa pide al usuario los valores a, b y c y calcule y muestre el área del triángulo.")
lado_a=float(input("Dame la longitud del lado a en centímetros: "))
lado_b=float(input("Dame la longitud del lado b en centímetros: "))
lado_c=float(input("Dame la longitud del lado c en centímetros: "))
s= (lado_a+lado_b+lado_c)/2
area_tri= math.sqrt(s*(s-lado_a)*(s-lado_b)*(s-lado_c))
print(f"El área del triangulo es: {area_tri: .2f} cm{up}")
