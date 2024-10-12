"""Este programa recibe horas, minutos y segundos, regresa equivalente en segundos.
P. Abigail Velarde Rodriguez A01646395"""

def equivalente(h,m,s):
    segundos= h*3600 + m*60 + s
    return segundos

def main():
    print("Este programa recibe horas, minutos y segundos, regresa equivalente en segundos.")
    h= int(input("Dame las horas: "))
    m= int(input("Dame los minutos: "))
    s= int(input("Dame los segundos: "))
    segundos= equivalente(h,m,s)
    print(f"La cantidad de segundos es: {segundos}")
    
main()