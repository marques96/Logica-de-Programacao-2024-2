resposta = "S"
soma_nota = 0
cont = 0

while resposta == "S":
    nota = float(input("Digite a nota do aluno: "))
    soma_nota += nota
    cont += 1
    resposta = input("Quer entrar com outra nota? [S/N]")

    print(f"A média das notas é : {nota}")