vel = float(input('velocidade marcada em km/h: '))
if vel > 80:
    print('voce exedeu o limite de velocide de 80Km/h. sera multado em R${:.2f}'.format((vel-80) * 7.00))
else:
    print('velocidade dentro do limite') 
