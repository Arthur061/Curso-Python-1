pm = float(input('\033[33mPrimeira média do aluno: '))
pd = float(input('Segunda nota do aluno: '))
pm1 = (pm + pd) / 2

print('A média entre \033[4;32m{:.1f}\033[m \033[33m e \033[m \033[4;32m {:.1f} \033[m \033[33m é \033[m \033[33m igual a \033[m \033[4;32m{:.1f}'.format(pm, pd, pm1))
