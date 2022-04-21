num = int(input('\033[33mDigite um número: '))
m1 = num-1
m2 = num+1

print('Analisando o número escolhido... Seu antecessor é \033[4;31m{}\033[m \033[33m e seu sucessor é \033[4;31m{}'.format (m1, m2))
