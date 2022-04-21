n1 = int(input('\033[36mEscolha um número: '))
n2 = int(input('Escolha outro número: '))
n3 = int(input('Escolha só mias um número agora: '))
if n1<n2 and n1<n3:
    menor = n1
if n2<n3 and n2<n1:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

if n1>n2 and n1>n3:
    maior = n1
if n2>n3 and n2>n1:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O menor número é \033[4;34m{}'.format(menor))
print('\033[0;36mO maior número é \033[4;34m{}'.format(maior))