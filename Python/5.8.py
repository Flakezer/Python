#Escreva um programa que leia dois números. Imprima o resultado da
#multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
#subtração para calcular o resultado. Lembre-se de que podemos entender a mul-tiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
#+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

num1= int(input("Digite o primeiro numero: "))
num2= int(input("Digite segundo numero: "))
resu = 0 

for c in range(0,num1):
    resu += num2
    
print(f"O resultado é: {resu}")