vlr_compra = float(input("Informe o total a pagar: R$"))
membro_fidelidade = input("Cliente faz parte do programa fidelidade? S/N ")
tem_cupom = input("Tem cupom de desconto? S/N ")


if (vlr_compra > 100) or (membro_fidelidade.upper() == "S") or (tem_cupom.upper() == "S"):
    print(True)
else:
    print(False)