""" Este programa recibe largo y ancho de un rectángulo, regresa area y perímetro.
P. Abigail Velarde Rodriguez A01646395"""

def perimetroRect(l,a):
    p= l*2 + a*2
    return p

def areaRect(l,a):
    a= l * a
    return a

def main():
    print("Este programa recibe largo y ancho de un rectángulo, regresa area o perímetro.")
    l= float(input("Dame el largo del rectángulo: "))
    a= float(input("Dame el ancho: "))
    clave= input("""Ingrese la clave de lo que desea calcular:
a. Area
p. Perimetro

Clave: """)
    if clave == "a":
        area= areaRect(l,a)
        print(f"El área es {area}")
        
    elif clave== "b":
        perimetro= perimetroRect(l,a)
        print(f"El perímetro es {perimetro}")
        
    else:
        print("Clave no válida.")
    
main()