numero = int(input("Digite um número: "))

resto = numero % 2

if(resto == 0):
    print(f"O número {numero} é par")
elif(resto == 1):
    print(f"O número {numero} é impar")