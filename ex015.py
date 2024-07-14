k = float(input('quantos Km foram percorridos com o carro: '))
d = int(input('quantos dias o carro foi alugados: '))
vt = (d * 60.00) + (k * 0.15)
print('consideranddo que o carro foi alugado por {} dias e foram rodados {}km o valor do aluguel vai ficar em R${:.2f}'.format(d,k,vt))
