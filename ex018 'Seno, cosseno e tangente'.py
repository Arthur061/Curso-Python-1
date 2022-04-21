import math
ang = float(input('\033[36mDigite um angulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('O angulo de \033[34m{} \033[36mtem o \n SENO de \033[34m{:.2f} \033[36m\n COSSENO de \033[34m{:.2f} \033[36m\n TANGENTE de \033[34m{:.2f}'.format(ang, seno, cosseno, tangente))