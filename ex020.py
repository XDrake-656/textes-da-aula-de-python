from random import sample
p1 = str(input('primeira aluno: '))
p2 = str(input('segunda aluno: '))
p3 = str(input('terceiro aluno: '))
p4 = str(input('quarto aluno: '))
n = sample([p1,p2,p3,p4], k=4)
print('apresentacoes serao feitas na ordem a seguir {}'.format(n))
