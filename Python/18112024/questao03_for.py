numero = int(input("Informe um número: "))

soma_numerador_crescente = 0

for i in range(1, numero + 1):
    soma_numerador_crescente += i / i 

print(f"Soma: {soma_numerador_crescente:.4f}")