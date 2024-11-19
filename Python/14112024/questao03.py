numero = int(input("Informe um número: "))

a = 0
b = 1
sequencia = 0

for i in range(numero - 2):
    sequencia = a + b
    a = b
    b = sequencia
    print(sequencia)