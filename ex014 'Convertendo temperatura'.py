inf = float(input('\033[32mInforme a temperatura em °C: '))

f = ((9 * inf)/5)+32

print('A temperatura de \033[31m{}°C \033[32mé convertida para \033[31m{}°F'
      .format(inf, f))
