num = int(input('\033[33mInforme um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[36mAnaliando o número \033[35m{}'.format(num))
print('\033[33mUnidade:\033[35m{} '.format(u))
print('\033[33mDezena: \033[35m{} '.format(d))
print('\033[33mCentena: \033[35m{}'.format(c))
print('\033[33mMilhar: \033[35m{}'.format(m))

