n1 = int(input('\033[0;34mDigite um valor: '))
n2 = int(input('\033[0;34mDigite outro número: \033[m'))
soma = n1+n2
print('A soma do número \033[4;31m{}\033[m e do número \033[4;31m{}\033[m é igual a \033[4;31m{}'.format (n1, n2, soma))