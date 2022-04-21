km = float(input('\033[34mDigite quantos km até seu destino: '))
km1 = km * 0.50 #até 200
km2 = km * 0.45 #mais d 200

if km <= 200:
    print('Olá, como sua viajem é \033[4;31mmenor\033[0;34m que 200km voce ira pagar um total de R${:.2f}'.format(km1))
else:
    print('Olá, sua viagem \033[4;31multrapassa\033[0;34m 200km então seu preço total a pagar será de R${:.2f}'.format(km2))
