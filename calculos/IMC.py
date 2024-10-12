"""
Este programa calcula el tiempo promedio en que una persona corre los lunes, miércoles y viernes.
INPUT:
t_lunes,t_miercoles,t_viernes
OUTPUT:
promedio
PROCESS:
1.-Este programa calcula el tiempo promedio en que una persona corre los lunes, miércoles y viernes.
2.- Imprimir "Dame el tiempo del lunes en minutos: ", guardarlo en t_lunes.
3.-Imprimir "Dame el tiempo del miercoles en minutos: ", guardarlo en t_miercoles.
4.-Imprimir "Dame el tiempo del viernes en minutos: ", guardarlo en t_viernes.
5.- Sumar los tres tiempos y dividirlo entre 3, guardarlo en promedio.
6.- Imprimir "Su promedio es de: ", imprimir IMC.
"""

print("Este programa calcula el tiempo promedio en que una persona corre los lunes, miércoles y viernes.")
t_lunes= float (input("Dame el tiempo del lunes en minutos: "))
t_miercoles= float (input("Dame el tiempo del miercoles en minutos: "))
t_viernes= float (input("Dame el tiempo del viernes en minutos: "))
Promedio= (t_lunes + t_miercoles + t_viernes)/3
print(f"Su promedio es de: {Promedio:.2f} minutos")