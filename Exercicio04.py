#verifica se um numero é perfeito

n = int(input("Digite um numero: "))
soma = 0 

for divisor in range(1,n):
    if n % divisor == 0:
        soma = soma + divisor
        
if n == soma:
    print("%d é um numero perfeito."%(n))
    
else:
    print("%d não é um numero perfeito."%(n))
