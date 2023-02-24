#Escreva um programa que pergunte a distância que um passageiro
#deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
#para viagens de até de 200 km, e R$ 0,45 para viagens mais longas

dist = int(input("Qual distância você deseja percorrer: "))

if dist<=200:
    pas = 0.50*dist
else: 
    pas = 0.45*dist

print(f"O valor a ser pago é: R${pas}")
