vlr_compra = float(input("Informe o valor final da compra: R$"))
desconto = 10/100

if(vlr_compra > 100.00):
    desconto = vlr_compra * desconto
    vlr_final = vlr_compra - desconto 
    print(f"O valor da compra R${vlr_compra:.2f} com desconto R${desconto:.2f} ficou com total: R${vlr_final:.2f}")