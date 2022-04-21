from random import choice
pa = str(input('\033[35mPrimeiro aluno: '))
sa = str(input('Segundo aluno: '))
ta = str(input('Terceiro aluno: '))
qa = str(input('Quarto aluno: '))
lista = [pa, sa, ta, qa]
escolhido = choice(lista)
print('O aluno escolhido foi \033[36m{}'.format(escolhido))
