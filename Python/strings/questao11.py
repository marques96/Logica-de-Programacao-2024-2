frase = input("Digite uma frase: ")
letra = input("Informe uma letra: ")

if(letra in frase):
    print(f"{letra} está contida em {frase}")
else:
    print(f"{letra} não está contida em {frase}")