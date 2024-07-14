from math import radians, sin, cos, tan
an = int(input('escreva um angulo qualquer: '))
x = radians(an)
s = sin(x)
c = cos(x)
t = tan(x)
print('o valor de seno coseno e a tangente de {}° é {:.2f}, {:.2f} e {:.2f} respectivamente'.format(an,s,c,t))
