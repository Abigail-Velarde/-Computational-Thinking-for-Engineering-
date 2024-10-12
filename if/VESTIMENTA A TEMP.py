print("Este programa determina cuál es la vestimenta más adecuada de acuerdo con la temperatura dada.")
temp=int(input("Dame la temperatura: "))
if temp >= 30:
    print("playera sin manga y short")
elif temp > 15:
    print("playera y jeans")
elif temp >= 0:
    print("sweater y pantalon")
else:
    print("gabardina y calentadores")