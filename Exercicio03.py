#Verica se um numero é tringular

numero = int(input("Insira um valor: "))

i = 1

if numero < 3:
    while True:
        print("Valor inválido. Tente novamente!")
        numero = int(input("Insira um valor: "))
        
        if numero >= 3:
            break

while i * (i + 1) * (i + 2) < numero:
    i += 1

if i * (i + 1) * (i + 2) == numero:
    print("{} é triangular, pois {} * {} * {} = {}".format(numero, i, i+1 ,i+2 ,numero))
else:
    print("{} não é um número triangular.".format(numero))
