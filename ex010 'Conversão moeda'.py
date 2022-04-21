real = float(input('\033[32mQuanto dinheiro voce tem na carteira? R$'))
soma = real / 5.28
print('Com \033[4;35mR${:.2f}\033[0;32m voce pode comprar \033[4;35mUS${:.2f}'.format(real, soma))
