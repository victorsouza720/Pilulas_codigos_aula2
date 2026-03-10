import random 
Cotação = float (input('Cotação atual do Dolar: '))
Variação = random.uniform(-0.015, 0.015)
nova_cotação = Cotação * (1 + Variação)
print (f'Variação simulada: {Variação: .3%}')
print (f'nova cotação: {nova_cotação: .2f}')
