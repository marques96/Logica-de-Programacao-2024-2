n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))
operacao = input("Informe a operação: [+|-|x|/] ")

if(operacao == "+"):
    adicao = n1 + n2
    print(f"A soma entre {n1} e {n2} é: {adicao}")
elif(operacao == "-"):
    subtracao = n1 - n2
    print(f"A subtração entre {n1} e {n2} é: {subtracao}")
elif(operacao == "x"):
    multiplicacao = n1 * n2
    print(f"A multiplicação entre {n1} e {n2} é: {multiplicacao}")
elif(operacao == "/"):
    divisao = n1 / n2
    print(f"A divisão entre {n1} e {n2} é: {divisao}")