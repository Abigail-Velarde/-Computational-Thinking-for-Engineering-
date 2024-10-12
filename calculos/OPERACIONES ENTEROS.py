""" Este programa pide dos números enteros y regresa el resultado de la operación seleccionada.
P. Abigail Velarde Rodriguez A01646395"""

def suma(num1,num2):
    s= num1 + num2
    return s

def resta(num1,num2):
    r= num1 - num2
    return r

def multi(num1,num2):
    m= num1 * num2
    return m

def div(num1,num2):
    d= num1 / num2
    return d

def main():
    print("Este programa pide dos números enteros y regresa el resultado de la operación seleccionada.")
    num1= int(input("Dame el primer numero entero: "))
    num2= int(input("Dame el segundo numero entero: "))
    clave= input("""Escoja las siguientes opciones:
1. s para suma
2. r para resta
3. m para multiplicación
4. d para división

Opción elegida: """)
    if clave == "s":
        resultado= suma(num1,num2)
        print(f"El resultado de su suma es: {resultado}")
    elif clave == "r":
        resultado= resta(num1,num2)
        print(f"El resultado de su resta es: {resultado}")
    elif clave == "m":
        resultado= multi(num1,num2)
        print(f"El resultado de su multiplicación es: {resultado}")
    elif clave == "d":
        resultado= div(num1,num2)
        print(f"El resultado de su división es: {resultado}")
    else:
        print("Clave no válida.")

main()