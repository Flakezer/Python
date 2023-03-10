#Altere o programa anterior para exibir os resultados no mesmo for-mato de uma tabuada: 2x1 = 2, 2x2=4, ...


c = 1
num = int(input("Digite seu numero: "))
while c <= 10:
    print(f'{num} x {c} = {num*c}')
    c += 1
