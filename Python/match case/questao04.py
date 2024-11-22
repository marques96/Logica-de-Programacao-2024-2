nota = float(input("Informe uma nota de 1 a 10: "))

match nota:
     case 10.0:
         print(f"Nota: {nota} Excelente")
     case _ if nota >= 9.0 and nota < 10.0:
         print(f"Nota: {nota} Muito Bom")
     case _ if nota >= 7.0 and nota < 9.0:
         print(f"Nota: {nota} Bom")
     case _ if nota >= 6.0 and nota < 7.0:
         print(f"Nota: {nota} Pode melhorar")
     case _ if nota >= 5.0 and nota < 6.0:
         print(f"Nota: {nota} Você está de recuperação!")
     case _ if nota >= 0.0 and nota < 5.0:
         print(f"Nota: {nota} Você está reprovado!")
     case _:
         print("Digite uma nota de 0 a 10!")