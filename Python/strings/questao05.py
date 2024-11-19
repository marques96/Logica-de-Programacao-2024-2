frase = input("Informe uma frase: ")

palindromo = ""

for letra in frase:
    palindromo = letra + palindromo
    
if(palindromo.upper() == frase.upper()):
    print(f"{frase} é palindromo: {palindromo.upper()}")
else:
    print(f"{frase} não é palindromo: {palindromo.upper()}")