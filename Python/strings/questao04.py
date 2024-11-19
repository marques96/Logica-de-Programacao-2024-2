frase = input("Informe uma frase: ")

nova_string = ""

for letra in frase:
        if letra != ' ':
            nova_string += letra
print(f"{frase} == {nova_string}")