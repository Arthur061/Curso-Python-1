from time import sleep
num = int(input('\033[34mDigite um número para saber de ele é par ou impar: '))
print('\033[4;31mPROCESSANDO...')
sleep(3)
resultado = num % 2

if resultado == 0:
    print('\033[0;34mO número \033[4;36m{}\033[0;34m é par'.format(num))
else:
    print('\033[0;34mSeu número \033[4;33m{}\033[0;34m é impar'.format(num))
