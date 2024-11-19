numero = 1
count = 0

while(numero != 0):
    numero = int(input("Informe um número: "))
    if(numero > 0):
        count +=1
print(f"{count} números positivos digitados")