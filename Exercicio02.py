print("Escolha uma das operações:\nAdição (1) Subtração (2) Multiplicação (3) Divisão (4).")

tipo = int(input("Numero: "))

if tipo == 1:
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite um valor: "))
    soma = n1 + n2
    print("O resultado da soma é %.2f" %(soma))
    
if tipo == 2:
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite um valor: "))
    menos = n1 - n2
    print("O resultado da subtração é %.2f" %(menos))
    
if tipo == 3:
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite um valor: "))
    mult = n1 * n2
    print("O resultado da multiplicação é %.2f" %(mult))
    
if tipo == 4:
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite um valor: "))
    if n2 != 0:
        div = n1 / n2
        print("O resultado da divisão e %.2f" %(div))
    else:
        print("Entrada invalida!!!")

