"""Este programa pide el valor del radio de un tatraedro y muestra su área.
INPUT
arista
OUTPUT
area
PROCESS
0.- Llamar a la librería que contiene a la raíz cuadrada, que es math
1.- Indicar que hace el programa
    Imprimir "Este programa pide el valor del a arista de un tetraedro y muestra su área."
2.- Imprimir "Dame el valor de la arista del tetraedro: ", guardar en radio.
3.- area = (arista**2)*(math.sqrt(3))
4.- Imprimir f "El área del tetraedro de arista {arista} es: {area: .3f} cm{up}"  """

import math
up="\u00B2"
print("Este programa pide el valor del a arista de un tetraedro y muestra su área.")
arista=float(input("Dame el valor de la arista del tetraedro: "))
area = (arista**2)*(math.sqrt(3))
print(f"El área del tetraedro de arista {arista} es: {area: .3f} cm{up}")