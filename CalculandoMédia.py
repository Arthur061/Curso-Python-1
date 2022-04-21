nome = str(input('Qual é o seu nome? '))
if nome == 'Arthur':
    print('Lindo, talves eu te ama mano')
    print('Bom dia, {}'.format(nome))
else:
    print('Puts mano... não te conheço :(')



n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))

if m >=5.0:
    print('Boa média, continue assim {}!'.format(nome))
    print('PS: voce é lindo, ok')
else:
    print('Puts em parceiro...')
    print('Sem comentarios para voce bro')



p1 = str(input('Digite o nome do professor(a) favorito: '))

if p1 == 'Arthur':
    print('Verdade!! Ele é bem legal :) #Obrigado')
else:
    print('Bom, acho que voce errou... O unico professor legal é o Arthur, tente melhor na proxima!! #Chateado')

p2 = str(input('Digite o nome de um professor chato: '))

if p2 == 'Arthur':
    print('Pare, eu não sou chato... Estou triste agora, obrigado :) #TristezaProfunda')
else:
    print('Verdade... ele é bem chato')



ano = int(input('Quantos anos voce tem? '))
print('Hm...interessante :)' if ano>=18 else 'Te vejo outra hora, tchau!')

