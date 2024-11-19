# Função para calcular o montante acumulado com juros compostos
def calcular_juros_compostos(deposito, taxa_juros, anos):
    montante = deposito * (1 + taxa_juros / 100) ** anos
    return montante

# Leitura dos dados de entrada
valor_deposito = float(input("Digite o valor do depósito bancário: R$ "))
taxa_juros_anual = float(input("Digite a taxa de juros anual (%): "))

# Cálculo dos valores acumulados após 1, 5 e 10 anos
anos = [1, 5, 10]
resultados = {}

for ano in anos:
    montante_acumulado = calcular_juros_compostos(valor_deposito, taxa_juros_anual, ano)
    resultados[ano] = montante_acumulado

# Exibição dos resultados
print("\nValor acumulado após:")
for ano, montante in resultados.items():
    print(f"{ano} ano(s): R$ {montante:.2f}")