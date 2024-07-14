from random import randint
from time import sleep
r = int(input('tente adivinhar um numero 0 a 5 que o computador escolher: '))
n = int(randint(0,5))
print('pensando....')
sleep(2)
if r == n:
    print('PARABENS voce acertou')
else:
    print('Você ERROU')
print('o numero sorteado escolhido pelo pc foi {}!'.format(n))
