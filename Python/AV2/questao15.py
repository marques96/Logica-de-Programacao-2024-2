n = int(input("Informe um número: "))
soma = 0 

for i in range(1,n+1):
    if(i % 2 == 0):
        soma = soma + i
        print(i)
print(soma)