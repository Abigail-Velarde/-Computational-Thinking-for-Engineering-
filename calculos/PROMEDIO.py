"""
Este programa calcula el promedio de 4 materias.

INPUT:
materia1, materia2, materia3, materia4

OUTPUT:
promedio

PROCESS:
1.-Este programa calcula el promedio de 4 materias
2.- Imprimir "Dame la calificaión de la primera materia: ", guardarlo en materia1.
3.- Imprimir "Dame la calificaión de la segiunda materia: ", guardarlo en materia2.
4.- Imprimir "Dame la calificaión de la tercera materia: ", guardarlo en materia3.
5.- Imprimir "Dame la calificaión de la cuarta materia: ", guardarlo en materia4.
6.- Sumar materia1, materia2, materia3, materia4, dividir entre 4, guardarlo en promedio.
8.- Imprimir "Promedio final: ", imprimir promedio.

"""

print("Este programa calcula el promedio de 4 materias")
materia1= float (input("Dame la calificaión de la primera materia: "))
materia2= float (input("Dame la calificaión de la segunda materia: "))
materia3= float (input("Dame la calificaión de la tercera materia: "))
materia4= float (input("Dame la calificaión de la cuarta materia: "))
promedio=(materia1 + materia2 + materia3 +materia4)/4
print(f"El promedio es: {promedio:.2f}")