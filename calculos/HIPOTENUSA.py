"""Este programa reciba los dos catetos de un triángulo rectángulo y encuentre su hipotenusa.
INPUT
cateto_a,cateto_b
OUTPUT
hipotenusa
Process
1.- Indicar que hace el programa
    Imprimir "Este programa reciba los dos catetos de un triángulo rectángulo y encuentre su hipotenusa."
2.- Imprimir "Dame la medida del cateto a en cm: ", guardar en cateto_a.
3.- Imprimir "Dame la medida del cateto b en cm: ", guardar en cateto_b.
5.- hipotenusa= math.sqrt((cateto_a**2)+(cateto_b**2))
6.- Imprimir resultados """

import math
print("Este programa reciba los dos catetos de un triángulo rectángulo y encuentre su hipotenusa.")
cateto_a=float(input("Dame la medida del cateto a en centímetros: "))
cateto_b=float(input("Dame la medida del cateto b en centímetros: "))
hipotenusa= math.sqrt((cateto_a**2)+(cateto_b**2))
print(f"La medida de la hipotenusa es de: {hipotenusa: .2f} cm")