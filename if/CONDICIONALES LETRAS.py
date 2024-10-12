print("Este programa recibe y compara dos letras proporcionadas por el usuario")
letra= input("Dame una letra: ")
letra2= input("Dame otra letra: ")

if letra > letra2 :
    print(f"{letra} es mayor que {letra2}")
    
elif letra < letra2:
    print(f"{letra} es menor que {letra2}")

else:
    print("Las dos letras son iguales")