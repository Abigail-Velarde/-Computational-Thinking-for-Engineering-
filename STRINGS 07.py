def inicio():
    cadena="Es muy facil programar en Python"

    for indice in range(len(cadena)):
        print(cadena[indice])



def compara1():
    lista=["Mexico","Brasil","Peru"]
    cadena=",".join(lista)
    print(lista)
    print(cadena)
    cadena2="---".join(lista)
    print(cadena2)
    
def compara2():
    nombreString='Diego David Avalos'
    nombreLista=nombreString.split()
    print(nombreLista)
    nombreString2='''Diego
David
Avalos'''
    nombreLista2=nombreString2.split(sep='\n')
    print(nombreLista2)

def contar_letras():    
    nombre= input("Escribe tu nombre: ")
    cuenta_letras=0
    for letra in nombre:
        print(letra)
        cuenta_letras += 1
    print(f"Tu nombre {nombre}, tiene {cuenta_letras} letras.")

def busca_letras():
    texto=input("Introduce un texto: ")
    texto=texto.lower()
    valor=input("Letra a encontrar: ")
    cont=0
    for letra in texto:
        if letra == valor:
            cont += 1
    print(f"La letra {valor} se encontro {cont} veces.")

def alumnos():
    lista=["Hugo","Pedro","Juan","Daniel","Rene"]
    print("Lista de alumnos: ")
    for elemento in lista:
        print(elemento)

def remplazo():
    texto=input("Introduce un texto: ")
    texto=texto.lower()
    lista=list(texto)
    print(lista)
    for indice in range(len(lista)):
        if lista[indice] in "a":
            lista[indice]="A"
    nuevo="".join(lista)
    print(nuevo)

def mayuscula():
    cadena="bienvenido a mi aplicacion"
    print(cadena.capitalize())

def minuscula():
    cadena="Hola Mundo"
    print(cadena.lower())
    
def a_programar():
    oracion=input("Dame una frase para separar: ")
    contador=0
    lista=oracion.split()
    palabras=len(lista)
    print(f"Su oracion esta compuesta por {palabras} palabras.")  
    modificada=oracion.replace("t","7")
    modificada=modificada.replace("i","l")
    modificada=modificada.replace("a","*")
    modificada=modificada.replace("e","3")
    print(modificada)
    for i in range(lista):
        if len(i)>5:
            contador+=1
    print(f"Tu frase tiene {contador} palabras con mas de 5 letras")
    
def ejercicio1():
    texto=input("Introduce un texto: ")
    texto=texto.lower()
    cont=0
    for letra in texto:
        if letra == "a":
            cont += 1
        elif letra == "e":
            cont += 1
        elif letra == "i":
            cont += 1
        elif letra == "o":
            cont += 1
        elif letra == "u":
            cont += 1    
    print(f"Hay {cont} vocales.")
    
def ejercicio2():
    texto=input("Introduce un texto: ")
    texto=texto.lower()
    cont=0
    for letra in texto:
        if letra == "a":
            cont += 1
        elif letra == "e":
            cont += 1
        elif letra == "i":
            cont += 1
        elif letra == "o":
            cont += 1
        elif letra == "u":
            cont += 1    
    texto2=input("Introduce un texto: ")
    texto2=texto2.lower()
    cont2=0
    for letra in texto:
        if letra == "a":
            cont2 += 1
        elif letra == "e":
            cont2 += 1
        elif letra == "i":
            cont2 += 1
        elif letra == "o":
            cont2 += 1
        elif letra == "u":
            cont2 += 1    
    if cont>cont2:
        print("La primera frase tiene mas vocales.")
    else:
        print("La segunda frase tiene mas vocales.")

def ejercicio3():
    lista=[]
    n=int(input("Dame el numero de palabras que quieres en tu lista: "))
    for i in range(n):
        palabra=input("Dame la palabra que quieres agregar: ")
        
        

def main():
    #inicio()
    #contar_letras()
    #busca_letras()
    #alumnos()
    #remplazo()
    #compara1()
    #compara2()
    #mayuscula()
    #minuscula() 
    #a_programar()
    #ejercicio1()
    ejercicio2()
    
main()
