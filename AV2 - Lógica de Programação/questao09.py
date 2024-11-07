nota_final = float(input("Informe uma nota de 0 a 10: "))

if (nota_final >= 7 and nota_final <= 10.0):
    print(f"{nota_final} Aprovado :D")
elif (nota_final >= 5 and nota_final <= 6.9):
    print(f"{nota_final} Está em recuperação :/")
elif(nota_final < 5):
    print(f"{nota_final} Está reprovado D:")
else:
    print("Informe uma nota válida!")