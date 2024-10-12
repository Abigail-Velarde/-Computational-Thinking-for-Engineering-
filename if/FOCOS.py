print("""Este programa va a preguntar cuántas cajas de cada producto desea el cliente,
presentar el monto de compra, plantear las opciones de pago,
y presentar el pago elegido con el monto a pagar """)
n_alog= int(input("Dame las cajas de focos alógenos: "))
n_ah= int(input("Dame las cajas de focos ahorradores: "))
n_circ= int(input("Dame las cajas de focos ahorradores circulares: "))
pedido= (n_alog * 250) + (n_ah * 700) + (n_circ*1000)
if pedido <= 0:
    print(f"No hubo compra")
elif pedido <= 5000:
    print(f"Su total es: ${pedido: ,.2f} en una sola exhibición.")
elif pedido <= 30000:
    meses3= pedido/3
    print(f"Su total es: ${pedido: ,.2f} en una exhibición o 3 meses sin intereses de ${meses3: .2f}")
else:
    print(f"""Su total es: ${pedido: ,.2f}. Por esto puede elegir:
1. 5% de descuento
2. Pago a 9 meses sin intereses""")
    opcion= int(input("Elijo la opción: "))
    if opcion == 1:
        con_desc= pedido*0.95
        print(f"Su total es: ${con_desc: ,.2f}.")
    elif opcion == 2:
        meses9= pedido/9
        print(f"Serían 9 pagos sin intereses de ${meses9: ,.2f} cada uno.")
        