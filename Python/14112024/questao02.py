numero = int(input("Informe um número: "))

soma = 0
i = 0
# for i in range(0, numero + 1):
#     if(i % 2 != 0):
#         print(i)
#         soma += i
# print(soma)

while(i <= numero):
    if(i % 2 != 0):
         print(i)
         soma += i
    i += 1
print(soma)