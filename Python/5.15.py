pagar = 0 

while True:
    cod = int(input("digite o codigo do produto: "))
    preço = 0


    if cod == 0:
        break

    elif cod == 1:
        preço = 0.5
        
    elif cod == 2:
        preço = 1

    elif cod == 3:
        preço = 4

    elif cod == 5:
        preço = 7

    elif cod == 9:
        preço = 8
    else:
        print("codigo invalido")
    if preço != 0:     
        qnt = int(input("digite a quantidade de produtos: "))
        pagar += qnt*preço
 
print(f"o total a ser pago é:: {pagar}")