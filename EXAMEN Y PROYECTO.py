print("Este programa determina si a partir de las calificaciones de examen y proyecto el alumno está aprobado, condicionado o reprobado.")
examen=float(input("Dame la calificación del examen: "))
proyecto=float(input("Dame la calificación del proyecto: "))
if examen >= 80 and proyecto >= 80:
    print("APROBADO")
elif examen >= 70 and proyecto >= 50:
    print("CONDIDIONADO")
else:
    print("REPROBADO")