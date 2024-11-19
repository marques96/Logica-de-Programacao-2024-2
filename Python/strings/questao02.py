frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
count = 0

for letra in frase:
    if letra in vogais:
        count += 1

print(f"A quantidade de vogais em {frase} é: {count}")