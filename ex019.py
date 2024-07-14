from random import choices
p1 = str(input('primeira pessoa: '))
p2 = str(input('segunda pessoa: '))
p3 = str(input('terceira pessoa: '))
p4 = str(input('quarta pessoa: '))
n1 = choices([p1,p2,p3,p4], k=1)
print('sorteado: {}'.format(n1))
