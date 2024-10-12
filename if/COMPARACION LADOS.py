print("Este programa muestre en la pantalla el tipo de triángulo de que se trata o si no es un triangulo.")
x= int(input("Dame el primer lado: "))
y= int(input("Dame el segundo lado: "))
z= int(input("Dame el tercer lado: "))

if X>0 and Y>0 and Z>0:
    
    if X + Y > Z and X + Z > Y and Y + Z > X:
        
        if X==Y and Y==Z:
            
            print("Es un triángulo equilatero.")
            
        elif (X==Y and X!=Z) or (Y==Z  and Y!=X) or (Z==X and Z!=Y):
            
            print("Es un triángulo isóceles.")
        
        elif X!=Z and Z!=Y and X!=Y:
            
            print("Es un triángulo escaleno")
        else:
            print("No es un triangulo")
    else:
        print("No es un triangulo")
else:
    print("No es un triangulo")
