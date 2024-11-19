numero = int(input("Informe um número: "))

soma_quadrados = 0

for i in range(1, numero + 1):
    soma_quadrados += (1 / (i**2)) 
    print(f"Nº {i} Soma: {soma_quadrados:.4f}")