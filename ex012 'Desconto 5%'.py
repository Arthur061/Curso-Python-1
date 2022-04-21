preço = float(input('\033[32mQual o preço do produto? R$'))
soma = preço - (preço * 5 / 100)
print('Com o desconto de 5% o preço do produto fica \033[31mR${}'.format(soma))
