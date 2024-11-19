numero = int(input("Informe um número: "))

s = 0
cont = 1

for k in range(1, numero + 1):
    termo = (-1)**(k + 1) * (k / (2 * k - 1))
    s += termo
print(f"O valor de S é {s:.4f}")