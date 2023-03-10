div = float(input("Digite o valor divida inicial: ")) 
jur = float(input("Digite os juros mensais: ")) 
jurm = float(input("Digite o valor que sera pago mensalmente: "))
msp = pago = 0

if jur >= msp:
    print("valor pago não suficiente")
else:
    while div>=0:
        div += jur
        div -= jurm
        msp += 1
        pago += jurm

print(f"O numero de meses pagos foi {msp} e o total pago foi R${pago} e o total de juros pago {jur*msp}")
