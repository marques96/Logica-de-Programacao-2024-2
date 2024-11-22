valor1 = int(input("Informe o 1º número: "))
valor2 = int(input("Informe o 2º número: "))
operacao = input("Informe uma operação matemática: ")
resultado = 0

match operacao:
    case "+":
        resultado = valor1 + valor2
        print(f"{valor1} + {valor2} = {resultado}")
    case "-":
        resultado = valor1 - valor2
        print(f"{valor1} - {valor2} = {resultado}")
    case "*":
        resultado = valor1 * valor2
        print(f"{valor1} * {valor2} = {resultado}")
    case "/":
        if valor2 != 0:
            resultado = valor1 / valor2
            print(f"{valor1} / {valor2} = {resultado}")
        else:
            print("Erro divisão por 0")
    case _:
        print("Informe uma operação válida!")