while True:
    a = int(input("valor 1: "))
    b = int(input("valor 2: "))
    c = int(input("valor 3: "))

    if (a>b) and (a>c):
        print(f"o maior valor é: {a} ")
    elif (a<b) and (a<c):
        print(f"o menor valor é: {a} ")
    

    if (b>a) and (b>c):
        print(f"o maior valor é: {b} ")
    elif (b<a) and (b<c):
        print(f"o menor valor é:{b}  ")


    if (c>a) and (b<c):
        print(f"o maior valor é: {c} ")
    elif (a>c) and (b>c):
        print(f"o menor valor é: {c} ")
