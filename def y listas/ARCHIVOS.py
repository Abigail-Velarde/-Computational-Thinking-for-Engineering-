"""Calificaciones"""

f=open("answers.csv","r")
respuestas=[]
for row in f:
    print(repr(row))
    respuestas.append(row)
f.close

