from math import sqrt
from math import pow
print("Este programa resuelve ecuaciones cuadráticas.")
a=float(input("Dame el valor de a: "))
b=float(input("Dame el valor de b: "))
c=float(input("Dame el valor de c: "))
if a == 0:
    if b ==0:
        print("No es una ecuación")
    else:
        x=-c/b
        print(f"El resultado es: {x}")
else:
    raiz= pow(b,2)-4*a*c
    if raiz < 0:
        print("Solución imaginaria")
    else:
        if raiz > 0:
            x1= ((-b) + (sqrt (raiz)))/(2*a)
            x2= ((-b) - (sqrt (raiz)))/(2*a)
            print(f"x1= {x1}")
            print(f"x2= {x2}")
        else:
            res= -b/2*a
            print("Ambas son iguales a: {res}")
            