soma = 0 #contador de soma
for n in range(1, 101):
    if(n % 2 != 0) and (n % 3 != 0):
        soma += n
        print(soma, end= ", ")