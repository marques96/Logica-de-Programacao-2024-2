numero = int(input("Informe um número: "))

s = 0

for i in range(1, numero + 1):
    if i % 2 == 0:  
        s -= 1 / i
    else:           
        s += 1 / i
    print(f"Nº {i} soma: {s:.4f}")