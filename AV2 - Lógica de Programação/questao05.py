idade = int(input("Informe a idade: "))

if (idade > 0 and idade <= 12):
    print(f"{idade} anos. Criança")
elif(idade >= 13 and idade <= 17):
    print(f"{idade} anos. Adolescente")
elif(idade >= 18):
    print(f"{idade} anos. Adulto")
else:
    print("Informe uma idade válida!")