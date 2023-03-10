def operacoes():
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

operacoes()