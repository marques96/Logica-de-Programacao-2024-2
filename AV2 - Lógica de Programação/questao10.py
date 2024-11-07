numero = int(input("Informe um número: "))

if(numero % 3 == 0 and numero % 5 == 0):
    print(f"{numero} é divisível por 3 e 5 ao mesmo tempo.")
else:
    print(f"{numero} não é divisível por 3 e 5.")