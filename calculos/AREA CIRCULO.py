"""Este programa pide el valor del radio de un círculo y muestra su área.
INPUT
radio
OUTPUT
area, volumen
PROCESS
0.- Llamar a la librería que contiene a PI, que es math
1.- Indicar que hace el programa
    Imprimir "Este programa pide el valor del radio de un círculoy muestre su área y su volumen."
2.- Imprimir "Dame el valor del radio del círculo: ", guardar en radio.
3.- area = pi*pow(radio,2)
4.- Imprimir f "El área de la esfera de radio {radio} es: "  """

import math
up="\u00B2"
print("Este programa pide el valor del radio de un círculo y muestra su área.")
radio=float(input("Dame el valor del radio del círculo: "))
area = (math.pi)*pow(radio,2)
print(f"El área de la esfera de radio {radio} es: {area: .3f} cm{up}")
