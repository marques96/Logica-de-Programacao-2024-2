numero = int(input("Informe um número: "))

frações_inversas = 0
cont = numero

while(cont > 0):
    frações_inversas += 1 / cont
    cont -= 1
print(f"A soma das frações inversas de {numero} até 1 é: {frações_inversas:.6f}")