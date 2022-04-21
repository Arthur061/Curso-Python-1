largura = float(input('\033[35mLargura da parede: '))
altura = float(input('\033[35mAltura da parede: '))
area = largura * altura
tinta = area / 2
print ('Como cada lata de tinta tem 1L e consegue pinta 2m² \n Para pintar a sua parede de \033[4;31m{:.2f}x{:.2f}, \033[0;35mtotalizando \033[4;31m{:.2f}m²\n \033[0;35mPrecisara de um total de \033[4;31m{:.2f}L \033[0;35mde tinta'.format(largura, altura, area, tinta))
