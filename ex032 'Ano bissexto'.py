from datetime import date
ano = int(input('\033[33mQual ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de \033[4;32m{}\033[0;33m é BISSEXTO'.format(ano))
else:
    print('O ano de \033[4;32m{}\033[0;33m não é BISSEXTO'.format(ano))
