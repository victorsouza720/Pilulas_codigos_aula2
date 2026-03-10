import statistics
lote1 = float (input('produçao lote 1: '))
lote2 = float (input('produçao lote 2: '))
lote3 = float (input('produçao lote 3: '))
media = statistics.mean((lote1, lote2, lote3))
desvio = statistics.stdev ((lote1, lote2, lote3))
print (f'media {media :.2f}')
print (f'Desvio padrão {desvio:.2f}')
