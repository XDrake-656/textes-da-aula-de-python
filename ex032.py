from datetime import date
ano = int(input('qual ano voce quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é um  ano bissexto'.format(ano))
else:
    print('o ano {} NÃO e um ano bissexto'.format(ano))
