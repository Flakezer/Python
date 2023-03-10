num1= int(input("Digite o primeiro numero: "))
num2= int(input("Digite segundo numero: "))
quo = 0
res = num1

while res >= num2:
    res -= num2
    quo += 1


print(f"O resultado é: {quo}")
print(f"O resto é: {res}")