d = int(input('escreva quantos quilometros seram percorridos na viagem: '))
if d <= 200:
    print('o valor da passagem ficara em R${:.2f}'.format(d * 0.50))
else:
    print('o valor da passagem ficara em R${:.2f}'.format(d * 0.45))

#forma mais simplificada

'''distancia = float(input('qual é adistancia da sua viagem? '))
print('voce esta prestes a começar uma viagem de {}Km/h'.format(distancia))
preço = distancia * 0.50 if distancia <= 200  else distancia * 0.45
print('É o preço da sua passagem sera de R${:.2f}'.format(preço))'''
