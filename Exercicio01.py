print("Equação do 2° com todos os termos. Ex: 2x² + 8x -24 = 0")

a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))

delta = (b*b) - 4 * a *(c)
raiz = delta ** 0.5
x1 = (-b + raiz) / (2 * a)
x2 = (-b - raiz) / (2 * a)

print("Δ = %d\nX¹ = %d\nX² = %d" %(delta, x1, x2))
