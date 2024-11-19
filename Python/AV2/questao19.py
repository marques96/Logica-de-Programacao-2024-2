quantidade = int(input("Informe quantos números deseja inserir: "))
numero_digitado = 1
media = 0

while(numero_digitado <= quantidade):
    numero = int(input("Digite um número: "))
    numero_digitado += 1
    media = numero / numero_digitado
print(media)