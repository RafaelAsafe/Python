" exercício 79 "

X = 'S'
l = []
while X in 'Ss':
    v = int(input('Insira um valor na lista \n'))
    if v in l:
        print('O valor já existe na lista, não sera incluido')
    else:
        l.append(v)
    X = (input('Quer continuar[S/N] \n'))
l.sort()
print(f'Os valores digitados foram {l}')
