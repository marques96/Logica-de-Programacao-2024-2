print(" 1- Consultar Saldo \n 2- Realizar Saque \n 3- Realizar Depósito \n 0- Sair")
escolha = int(input("Escolha uma opção: "))
saldo = 0.00

while (escolha != 0):
    if (escolha == 1):
        print(f"Seu saldo é: {saldo:.2f}")
    
    if (escolha == 2):
        if saldo == 0.0:
            print(f"R${saldo:.2f} Saldo insuficiente! Realize um depósito.")
        else:
            valor_saque = float(input("Digite o valor do seu saque: "))
            if (valor_saque > saldo):
                print("Operação não permitida. Valor do saque é superior ao saldo!")
            else: 
                saldo -= valor_saque
                print(f"Sucesso! Você sacou R${valor_saque}, Seu saldo é R${saldo:.2f}")
    if (escolha == 3):
        valor_deposito = float(input("Informe um valor para depósito: "))
        saldo += valor_deposito
        print(f"Você depositou R${valor_deposito:.2f}, seu saldo atual é R${saldo:.2f}")
        
        
    print("\n 1- Consultar Saldo \n 2- Realizar Saque \n 3- Realizar Depósito \n 0- Sair")
    escolha = int(input("Escolha uma opção: "))
        

    if (escolha == 0):
        print("Até a próxima... :D")