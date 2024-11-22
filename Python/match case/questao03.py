idade = int(input("Informe sua idade: "))

match idade:
    case _ if idade <= 10:
        print(f"Idade: {idade} categoria: Criança")
    case _ if idade > 10 and idade < 14:
        print(f"Idade: {idade} categoria: Pré-adolescente")
    case _ if idade >= 14 and idade < 18:
        print(f"Idade: {idade} categoria: Adolescente")
    case _ if idade >= 18:
        print(f"Idade: {idade} categoria: Adulto")