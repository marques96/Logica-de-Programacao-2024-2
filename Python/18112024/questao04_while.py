numero = int(input("Informe um número: "))

soma_quadrados = 0
cont = 1

while(cont <= numero):
    soma_quadrados += (1 / (cont**2))
    cont += 1 
    print(f"Nº {cont} Soma: {soma_quadrados:.4f}")