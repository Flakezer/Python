#Escreva um programa que leia dois números e que pergunte qual
#operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
#multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

while True:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    op = input("Qual operação você deseja realizar (+,-.*,/): ")

    if op == "+":
        print(f"Resultado: {n1+n2}")
    elif op == "-":
        print(f"Resultado: {n1-n2}")    
    elif op == "*":
        print(f"Resultado: {n1*n2}")
    elif op == "/":
        print(f"Resultado: {n1/n2}")
    else: 
        print("operação ivalida")


