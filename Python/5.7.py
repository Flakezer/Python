#Modifique o programa anterior de forma que o usuário também
#digite o início e o fim da tabuada, em vez de começar com 1 e 10.
#


num = int(input("Digite seu numero: "))
inicio = int(input("Qual o inicio da tabuada: "))
fim = int(input("Qual o fim da tabuada: "))
while inicio <= fim:
    print(f'{num} x {inicio} = {num*inicio}')
    inicio += 1
