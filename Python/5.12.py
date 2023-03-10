depi = float(input("Digite o valor do deposito inicial: ")) 
tax = float(input("Digite taxa da poupança: ")) 
final = depi
depm = float(input("Digite o valor que sera depositado mensalmente: "))


for c in range(0,24):
    final += depm+final*(tax/100)
    print(f"Valor que a poupança arrecadou no {c+1}° mes: R${final:.2f}")

print(f"O ganho toal foi: {final- depi:.2f}")
