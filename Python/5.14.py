lista = []
while True:
    num = int(input('Digite um número(0 para parar): '))
    if num == 0:
        break
    lista.append(num)
    
print(f'a quantidade de números {len(lista)}')
print(f'a soma dos números {sum(lista)}')
print(f"a media do numeros é {sum(lista)/len(lista)}")