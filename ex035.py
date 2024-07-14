print('-=-' * 20)
print('analisador de triangulo')
print('-=-' * 20)
l1 = float(input('primeiro lado: '))
l2 = float(input('segundo lado: '))
l3 = float(input('terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2: 
    print('Com esses sgmentos de reta é SIM possivel criar um trialgulo')
else:
    print('Com esses segmentos de reto NÃO é possivel criar um triangulo')
