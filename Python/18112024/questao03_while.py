numero = int(input("Informe um número: "))

soma_numerador_crescente = 0
cont = 1

while(cont <= numero):
    soma_numerador_crescente += cont / cont 
    cont += 1

print(f"Soma: {soma_numerador_crescente:.4f}")