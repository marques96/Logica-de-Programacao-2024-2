numero = int(input("Informe um número: "))

soma_harmonica = 0
cont = 1

while (cont <= numero):
    soma_harmonica = soma_harmonica + 1 / cont
    print(f"Nº {cont} soma: {soma_harmonica:.4f}")
    cont += 1