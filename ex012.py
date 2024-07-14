p = float(input('digite o preço do produto: '))
d = (p * 5) / 100
vf = p - d
print('o preço do produto é R${:.2f} e seu desconto e de R${:.2f} assim seu valor final sera de R${:.2f}'.format(p,d,vf))
