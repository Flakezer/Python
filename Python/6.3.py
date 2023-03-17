lista1 = [0,1,2]
lista2 = [2,4,5]


lista1.extend(lista2)
lista3 = []

for i in lista1:
    if i not in lista3:
        lista3.append(i)

print(lista3)