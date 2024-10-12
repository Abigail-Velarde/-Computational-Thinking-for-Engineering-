texto= " Always an angel, never a god "
texto2=texto.strip()
print(texto2)


texto3=texto2.split(" ")
print(texto3)
texto3[5]="goddess"
print(texto3)
texto4=" ".join(texto3)
print(texto4)
for palabra in texto3:
     print(palabra)

