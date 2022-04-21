import random
n1 = str(input('\033[33mPrimeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print('A ordem de apresentaçao é\033[36m ')
print(lista)
