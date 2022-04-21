km = float(input('\033[31mQuantos km voce rodou com o carro? '))
dia = int(input('Quantos dias voce rodou com o carro? ' ))
dia1 = 60 * dia
km1 = 0.15 * km
valor = km1 + dia1

print('O total a pagar será de: \033[36mR${:.2f}'.format(valor))