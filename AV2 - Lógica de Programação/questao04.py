ano = int(input("Informe um ano: "))

if(ano % 4 == 0) and (ano % 100 != 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é bissexto.")