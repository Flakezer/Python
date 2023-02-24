#Escreva um programa que pergunte o salário do funcionário e calcule
#o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
#10%. Para os inferiores ou iguais, de 15%.


sala = float(input("digite seu salário:  "))

if sala>=1250: 
    print(f"seu salário agora é: {sala+sala*0.10}  ")
else:
    print(f"seu salário agora é: {sala+sala*0.15}  ")    