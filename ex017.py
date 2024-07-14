'''from math import sqrt
x = float(input('comprimento do cateto oposto: '))
y = float(input('comprimento do cateto adjacente: '))
ch = sqrt ((x*x) + (y*y))
print('sendo cateto oposto {} e cateto adjacente {} a hipotenusa é {:.2f}'.format(x,y,ch))'''

# ou pode ser feito de outa forma

from math import hypot
x = float(input('comprimento do cateto oposto: '))
y = float(input('comprimento do cateto adjacente: '))
ch = hypot(x,y)
print('sendo cateto oposto {} e cateto adjacente {} a hipotenusa é {:.2f}'.format(x,y,ch))
