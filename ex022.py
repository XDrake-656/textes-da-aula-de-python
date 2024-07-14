n = str(input('escreva seu nome completo: ')).strip()
div = n.split()
print('analisando seu nome...')
print('Este é seu nome em maiuscula: {}'.format(n.upper()))
print('este é seu nome em minuscula: {}'.format(n.lower()))
print('e possui {} letras'.format(len(''.join(div))))
print('e seu primeiro nome é {} e possui {} letras'.format(div[0],len(div[0])))



# tambem pode ser resolvido dessa maneira:
'''print('seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
print('seu primeiro nome tem {} letras'.format(n.find(' ')))'''
