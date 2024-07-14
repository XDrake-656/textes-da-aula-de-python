f = str(input('nome do funcionario: '))
v = float(input('valor do salario recebido:R$ '))
vf = v + ((v * 15) / 100)
print('{} recebe R${:.2f} porem recebeu um aomento de 15% assim sendo seu salario aumentara para R${:.2f}'.format(f,v,vf))
