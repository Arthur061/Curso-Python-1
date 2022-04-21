medida = float(input('\033[33mUma distancia em metro: '))
cm = medida*100
mm = medida*1000
dm = medida*10
dam = medida/10
hm = medida/100
km = medida/1000

print('A medida \033[4;36m{}m\033[m \033[33mcorresponde a\033[m \033[4;36m\n {}cm \n {}mm \n {}dm \n {}dam \n {}hm \n {}km'.format(medida, cm, mm, dam, dm, hm, km))
