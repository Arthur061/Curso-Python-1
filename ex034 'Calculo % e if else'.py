salario = float(input('\033[33mQual é o seu salario? R$ '))
s1 = salario + (salario * 10 / 100) #+1250
s2 = salario + (salario * 15 / 100) #-1250
if salario <= 1250:
    print('Seu salario era de \033[4;36mR${:.2f}\033[0;33m e voce recebera um aumento de 15%. Seu salario atual é de \044[4;36mR${:.2f}'.format(salario, s2))
else:
    print('\033[0;33mSeu salario era de \033[4;36mR${:.2f}\033[0;33m e voce recebera um aumento 10%. Seu salario atual é de \033[4;36mR${:.2f}'.format(salario, s1))