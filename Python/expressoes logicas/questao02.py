ingresso = input("Tem ingresso? [S/N] ")
idade = int(input("Informe sua idade: "))

if (idade < 18):
    autorizacao = input("Tem autorização de pai ou responsável? [S/N] ")

if(ingresso.upper() == "S") or (idade >= 18) or (autorizacao.upper() == "S"):
    print(True)
else:
    print(False)