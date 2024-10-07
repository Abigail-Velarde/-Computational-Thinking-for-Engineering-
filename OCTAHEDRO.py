"""Este programa pide el valor del radio de un octahedro y muestra su volumen.
INPUT
arista
OUTPUT
volumen
PROCESS
0 Llamar a la librería que contiene a la raíz cuadrada, que es math
1 Indicar que hace el programa
    Imprimir "Este programa pide el valor del a arista de un octahedro y muestra su volumen."
2 Imprimir "Dame el valor de la arista del octahedro en centímetro: ", guardar en arista.
4 volumen= ((math.sqrt(2))/3)*(arista**3)
4 Imprimir f "El área del octahedro con una arista de {arista} es: {volumen: .3f} cm{up}"  """

import math
up="\u00B3"
print("Este programa pide el valor del a arista de un octahedro y muestra su volumen.")
arista=float(input("Dame el valor de la arista del octahedro en centímetros: "))
volumen= ((math.sqrt(2))/3)*(math.pow(arista,3))
print(f"El volumen del octahedro con una arista de {arista} es: {volumen: .3f} cm{up}")