numero = int(input("Informe um número: "))

if(numero > 1):
    if (numero % 2 == 0):
        print(f"{numero} não é primo")
    else:
        print(f"{numero} é primo")