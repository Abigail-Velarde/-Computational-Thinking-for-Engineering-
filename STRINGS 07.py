# Este programa tiene varias funciones para trabajar con strings y listas

def inicio():
    # Esta función muestra cada letra de una frase
    cadena="Es muy facil programar en Python"
    for indice in range(len(cadena)):
        print(cadena[indice])

def compara1():
    # Aquí juntamos palabras de una lista con diferentes separadores
    lista=["Mexico","Brasil","Peru"]
    cadena=",".join(lista)
    print(lista)
    print(cadena)
    cadena2="---".join(lista)
    print(cadena2)
    
def compara2():
    # Esta función divide strings en listas de diferentes formas
    nombreString='Diego David Avalos'
    nombreLista=nombreString.split()
    print(nombreLista)
    nombreString2='''Diego
David
Avalos'''
    nombreLista2=nombreString2.split(sep='\n')
    print(nombreLista2)

def contar_letras():    
    # Cuenta cuántas letras tiene un nombre
    nombre= input("Escribe tu nombre: ")
    cuenta_letras=0
    for letra in nombre:
        print(letra)
        cuenta_letras += 1
    print(f"Tu nombre {nombre}, tiene {cuenta_letras} letras.")

def busca_letras():
    # Busca cuántas veces aparece una letra en un texto
    texto=input("Introduce un texto: ")
    texto=texto.lower()
    valor=input("Letra a encontrar: ")
    cont=0
    for letra in texto:
        if letra == valor:
            cont += 1
    print(f"La letra {valor} se encontro {cont} veces.")

def alumnos():
    # Imprime una lista de alumnos
    lista=["Hugo","Pedro","Juan","Daniel","Rene"]
    print("Lista de alumnos: ")
    for elemento in lista:
        print(elemento)

def remplazo():
    # Cambia todas las 'a' por 'A' en un texto
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
    # Pone en mayúscula la primera letra de una frase
    cadena="bienvenido a mi aplicacion"
    print(cadena.capitalize())

def minuscula():
    # Pone en minúsculas toda una frase
    cadena="Hola Mundo"
    print(cadena.lower())
    
def a_programar():
    # Hace varias cosas con una frase: la separa, cuenta palabras, reemplaza letras
    oracion=input("Dame una frase para separar: ")
    contador=0
    lista=oracion.split()
    palabras=len(lista)
    print(f"Su oracion esta compuesta por {palabras} palabras.")  
    modificada=oracion.replace("t","7").replace("i","l").replace("a","*").replace("e","3")
    print(modificada)
    for palabra in lista:
        if len(palabra)>5:
            contador+=1
    print(f"Tu frase tiene {contador} palabras con mas de 5 letras")
    
def ejercicio1():
    # Cuenta las vocales en un texto
    texto=input("Introduce un texto: ")
    texto=texto.lower()
    cont=0
    for letra in texto:
        if letra in "aeiou":
            cont += 1
    print(f"Hay {cont} vocales.")
    
def ejercicio2():
    # Compara la cantidad de vocales en dos frases
    texto=input("Introduce un texto: ")
    texto=texto.lower()
    cont=sum(1 for letra in texto if letra in "aeiou")
    texto2=input("Introduce un texto: ")
    texto2=texto2.lower()
    cont2=sum(1 for letra in texto2 if letra in "aeiou")
    if cont>cont2:
        print("La primera frase tiene mas vocales.")
    elif cont==cont2:
        print("Ambas frases tienen la misma cantidad de vocales.")
    else:
        print("La segunda frase tiene mas vocales.")

def ejercicio3():
    # Crea una lista de palabras y busca cuántas veces aparece una palabra
    lista = []
    n = int(input("Dame el numero de palabras que quieres en tu lista: "))
    for i in range(n):
        palabra = input("Dame la palabra que quieres agregar: ")
        lista.append(palabra)
    p_buscar = input("Dame la palabra que quieres buscar: ")
    rep = lista.count(p_buscar)
    print(f"La palabra '{p_buscar}' aparece {rep} veces en la lista.")

def ejercicio4():
    # Reemplaza una palabra por otra en una lista
    lista = []
    n = int(input("Dame el numero de palabras que quieres en tu lista: "))
    for i in range(n):
        palabra = input("Dame la palabra que quieres agregar: ")
        lista.append(palabra)
    print(lista)    
    p1=input("Dame la palabra que quieres remplazar: ")
    p2=input("Dame la nueva palabra: ")
    lista = [p2 if palabra == p1 else palabra for palabra in lista]
    print(lista)       

def ejercicio5():
    # Elimina una palabra de una lista
    lista = []
    n = int(input("Dame el numero de palabras que quieres en tu lista: "))
    for i in range(n):
        palabra = input("Dame la palabra que quieres agregar: ")
        lista.append(palabra)
    print("Lista original:", lista)    
    p1 = input("Dame la palabra que quieres eliminar: ")
    lista = [palabra for palabra in lista if palabra != p1]
    print("Lista después de eliminar:", lista)

def ejercicio6():
    # Divide una cadena con guiones cada cierto número de caracteres
    cadena = input("Introduce una cadena de texto: ")
    intervalo = int(input("Introduce el intervalo para dividir la cadena: "))
    
    segmentos = [cadena[i:i+intervalo] for i in range(0, len(cadena), intervalo)]
    resultado = "-".join(segmentos)
    
    print(f"Cadena original: {cadena}")
    print(f"Cadena dividida: {resultado}")

def main():
    # Aquí puedes elegir qué función quieres ejecutar
    """inicio()
    contar_letras()
    busca_letras()
    alumnos()
    remplazo()
    compara1()
    compara2()
    mayuscula()
    minuscula() 
    a_programar()
    ejercicio1()
    ejercicio2()
    ejercicio3()
    ejercicio4()
    ejercicio5()"""
    ejercicio6()

main()