salario = float(input('escreva seu salario? R$ '))
if salario > 1250.00:
    print('Você recebeu um aumento de 10% assim voce recebera R${:.2f} apartir de agora'.format(salario + ((salario * 10) / 100)))
else:
    print('Você recebeu um aumento de 15% assim voce recebera R${:.2f} apartir de agora'.format(salario + ((salario * 15) / 100)))
