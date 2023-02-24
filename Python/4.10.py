#Escreva um programa que calcule o preço a pagar pelo fornecimento
#de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de insta-
#lação: R para residências, I para indústrias e C para comércios. Calcule o preço a
#pagar de acordo com a tabela a seguir.

while True:
    kwh = int(input("Quantos Kwh são consumidos: "))
    inst = input("Qual sua instalação (R,I,C):")

    if inst == "R":
        if kwh>=500:
            print(f"Valor a pagar é: {kwh*0.40}")
        else:
            print(f"Valor a pagar é: {kwh*0.65}")
    elif inst == "I":
        if kwh>=500:    
            print(f"Valor a pagar é: {kwh*0.55}")
        else:
            print(f"Valor a pagar é: {kwh*0.60}")

    elif inst == "C":
        if kwh>=500:  
            print(f"Valor a pagar é: {kwh*0.55}")
        else:
            print(f"Valor a pagar é: {kwh*0.60}")
    else:
        print("Instalação invalida")


