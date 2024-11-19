numero = int(input("Informe um número para fatorial: "))
fatorial = 1

for i in range(numero, 0, -1):
    fatorial *= i
    print(i)
print(fatorial)