numero = int(input("Informe um número: "))

frações_inversas = 0

for i in range(numero, 0, -1):
    frações_inversas += 1 / i
print(f"A soma das frações inversas de {numero} até 1 é: {frações_inversas:.6f}")