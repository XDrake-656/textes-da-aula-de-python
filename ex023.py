# tentando com string
'''n = str(input('digite um numero de 0 a 9999: '))
print('o numero {} possui:\n unidades:{}\n dezenas:{}\n centenas:{}\n milhar:{}'.format(n,n[3],n[2],n[1],n[0]))'''

#resposta usando int
n = int(input('digite um numero ate 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('o numero {} possui:'.format(n))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
