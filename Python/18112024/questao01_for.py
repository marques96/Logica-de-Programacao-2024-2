numero = int(input("Informe um número: "))

soma_harmonica = 0

for i in range(1, numero + 1):
    soma_harmonica += 1 / i
    print(f"Nº {i} soma: {soma_harmonica:.4f}")