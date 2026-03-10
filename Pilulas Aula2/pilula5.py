import locale
locale.setlocale(locale.LC_ALL, 'pt_br.UTf-8')
r1 = float (input ('receita 1 :'))
r2 = float (input ('receita 2 :'))
r3 = float (input ('receita 3 :'))
total = r1 + r2 + r3
print (f' Mes 1 {locale.currency(r1,grouping=True)}')
print (f' Mes 2 {locale.currency(r2,grouping=True)}')
print (f' Mes 3 {locale.currency(r3,grouping=True)}')
print (f'total {locale.currency(total,grouping=True)}')