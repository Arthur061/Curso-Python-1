velocidade = float(input('\033[33mQual a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[31mPuts, multado irmão. Excedeu o limite de 80km/h. Total a pagar R${:.2f}'.format(multa))
else:
    print('\033[32mTa tranquilo boy, pode passar dboa ai. Nada de multa hoje, dirija com segurança.')
