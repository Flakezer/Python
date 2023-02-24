#Escreva um programa que pergunte a velocidade do carro de um
#usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
#foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
#80 km/h.
while True: 
    vel = int(input("digite a velocidade: "))

    if(vel>80):
        print(f"você foi multado: {(vel*5)-400}")
    elif (vel<0):
        print("você esta quebradando o espaço tempo")
    else: 
        print("você não foi multado")
