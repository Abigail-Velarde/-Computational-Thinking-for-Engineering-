"""Paula Abigail Velarde Rodriguez A01646395"""
def cot(servicio, mod, invitados): 
    if servicio == 1:
        if mod == 1:
            if invitados>=100:
                costo= invitados*700
                print(f"El costo de su evento sería de ${costo: ,.2f}")
                if invitados>500:
                    print("Se agregan 10 botellas de tequila de la casa.")
            else:
                print("No es posible cotizar eventos de menos de 100 invitados")
        else:
            if invitados>=100:
                costo= (invitados*700)*1.2
                print(f"El costo de su evento sería de ${costo:,.2f}")
                if invitados>500:
                    print("Se agregan 10 botellas de tequila de regalo por parte de la casa.")
            else:
                print("No es posible cotizar eventos de menos de 100 invitados")
    else:
        if mod == 1:
            if invitados>=100:
                costo= invitados*1500
                print(f"El costo de su evento sería de ${costo: ,.2f}")
                if invitados>500:
                    print("Se agregan 10 botellas de tequila de la casa.")
            else:
                print("No es posible cotizar eventos de menos de 100 invitados")
        else:
            if invitados>=100:
                costo= (invitados*1500)*1.3
                print(f"El costo de su evento sería de ${costo:,.2f}")
                if invitados>500:
                    print("Se agregan 10 botellas de tequila de regalo por parte de la casa.")
            else:
                print("No es posible cotizar eventos de menos de 100 invitados") 
def desc():
    descuento= randint(10,15)
    print(f"Su tarjeta de descuento es de {descuento}%")

def main():
    print("Este programa ayuda a pre-cotizar paquetes de eventos de la empresa Party durante la expo.")
    while True:
        opcion= int(input("""Elija la opción que le interese:
        1.-Pre-cotización
        2.-Descuento
        3.-Salir
        Opción: """))
        if opcion == 1:
            servicio= int(input("""Escoja un servicio:
                        1.- Cena de 3 tiempos
                        2.- Fiesta de 5 horas
                        Servicio: """))
            mod= int(input("""Escoja su modalidad deseada:
                    1.- Mexicana
                    2.- De lujo
                    Modalidad : """))
            invitados= int(input("Ingrese su cantidad de invitados: "))
            cot(servicio, mod, invitados)
        if opcion == 2:
            desc()
        if opcion == 3:
            print("Gracias, hasta pronto.")
            break

from random import randint
main()