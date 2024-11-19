numero = int(input("Informe um número: "))

s = 0
cont = 1

while( cont <= numero):
    if cont % 2 == 0:  
        s -= 1 / cont
    else:           
        s += 1 / cont
    
    cont += 1
    print(f"Nº {cont} soma: {s:.4f}")