sal = float(input('\033[33mQual p salário do funcionario ? R$'))
novo = sal + (sal * 15 / 100)
print('Um funcionario que ganhava \033[31mR${} \033[33mcom o aumento de 15% vai ganhar agora \033[31mR${:.2f}'.format(sal, novo))
