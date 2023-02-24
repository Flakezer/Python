#Escreva um programa para aprovar o empréstimo bancário para
#compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
#salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
#superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
#casa a comprar dividido pelo número de meses a pagar.
while True:
    valc = float(input("Qual o valor da casa que deseja comprar: "))
    sala = float(input("Qual o seu salário: "))
    ano = int(input("Quantos anos pretende ficar pagando: "))

    pres = valc/(ano*12)
    if pres<sala*0.30:
        print(f"O valor a pagar é: R${pres/(ano/12):.2f} por mês ")
    else:
        print("Você não consegue comprar a casa")


