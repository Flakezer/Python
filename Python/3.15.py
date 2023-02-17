cigd = int(input("quantidade de cigarros fumados por dia: "))
anof = int(input("quantidade de anos fumando: "))

print(f"dias perdidos: {((cigd*anof*365)*10)/1440:.0f}")
#.0f faz o numero com virgula ficar inteiro