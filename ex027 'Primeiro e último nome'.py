n = str(input('\033[33mDigite seu nome: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!!')
print('Seu primeiro nome é \033[4;36m{}'.format(nome[0]))
print('\033[0;33mSeu ultimo nome é \033[4;36m{}'.format(nome[len(nome)-1]))
