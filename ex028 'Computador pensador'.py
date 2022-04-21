from random import randint
from time import sleep

computador = randint(0, 5) #Faz o computador 'PENSAR'

print('\033[33m-=-' * 20)

print('\033[36mPensei em um número...')

jogador = int(input('\033[34mO computador pensou em um número de 0 a 5, tente adivinha!! Digite seu número: ')) #O jogador tenta adivinhar

print('\033[33m-=-' * 20)

print('\033[36mPROCESSANDO')
sleep(3)

if jogador == computador:
    print('\033[32mBoa, voce acertou o número')

else:
    print('\033[31mTa de boa boy, o computador é foda também. Pensei no número {} não no {}'.format(computador, jogador))

