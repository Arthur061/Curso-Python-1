frase = str(input('\033[32mDigite uma frase: ').upper()).strip()
print('A letra A apareceu \033[4;31m{} \033[0;32mvezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posiçao \033[4;31m{}'.format(frase.find('A')+1))
print('\033[0;32mA última letra A apareceu na posiçao \033[4;31m{}'.format(frase.rfind('A')+1))
