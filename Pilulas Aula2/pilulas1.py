import math
assinantes = int (input('Digite a qtd de assinantes: '))
mensalidade = float (input('O valor da mensalidade: '))
taxa = float(input('Digite a taxa de crescimento mensal %: '))
meses = int(input ('Digite a qtd de meses de projeção: '))
#processamento
assinantes_finais = assinantes *math.pow ((1 + taxa), meses)
receita_final = assinantes_finais * mensalidade
#saida
print (f'assinantes estimados:{assinantes_finais:.0f}')
print (f'receita esrtimada : R$ {receita_final:.2f}')

