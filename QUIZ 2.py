"""Paula Abigail Velarde Rodriguez A01646395
Este programa muestra las promociones y su aplicación en la compra del usuario."""

from random import randint
print("Este programa muestra las promociones y su aplicación en la compra del usuario.")
compra= float(input("Dame el total de tu compra: "))
if compra > 0 :
    opcion= int(input("""Escoga entre las dos promociones disponibles.
1. Pagar a meses sin intereses ó
2. Entrar a una tómbola de descuentos
Escoge la opción: """))
    if opcion == 1:
        meses= int(input("Escoja la cantidad de meses que quiera entre 6 y 12: "))
        if meses >= 6 and meses <=12:
            total= compra/meses
            print(f"Su compra de ${compra: .2f} equivaldría a {meses} pagos de ${total: .2f}")
        else:
            print("Número de meses no válido, vuelva a intentar.")
    else:
        numero=randint(1,3)
        if numero == 1:
            desc= 30
            preciof = compra * 0.70
            print(f"Con el número {numero} se ganó un descuento de {desc}% que deja su compra de ${compra: .2f} en ${preciof: .2f}")
        elif numero == 2:
            desc= 20
            preciof = compra * 0.80
            print(f"Con el número {numero} se ganó un descuento de {desc}% que deja su compra de ${compra: .2f} en ${preciof: .2f}")
        else:
            desc= 10
            preciof = compra * 0.90
            print(f"Con el número {numero} se ganó un descuento de {desc}% que deja su compra de ${compra: .2f} en ${preciof: .2f}")
else:
    print("No se marcó una compra, vuelva a intentar.")