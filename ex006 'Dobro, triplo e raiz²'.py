from math import sqrt
n = int(input('\033[32mDigite um número: '))
ns = n*2
n3 = n*3
n4 = sqrt(n)
print('O dobro de \033[31m{}\033[m \033[32m vale\033[m \033[31m{}\033[m'.format(n, ns))
print('\033[32mO triplo de\033[m \033[31m {} \033[32m \033[32m vale \033[m \033[31m{}\033[m'.format(n, n3))
print('\033[32mA raiz quadrada de\033[m \033[31m{}\033[m \033[32m é \033[m \033[31m{:.2f}'.format(n, n4))