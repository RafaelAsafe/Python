"exercício 72 mundo 3"

listanum = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze ou catorze', 'quinze', 'dezesseis',
            'dezesete', 'dezoito', 'dezenove', 'vinte')
R = 'S'
while R == 'S':
    while True:
        x = int(input('digite um número entre 0 e 20 \n'))
        if 0 <= x <= 20:
            break
        print('tente novamente.', end='')
    print(f'você digititou o número {listanum[x]}')
    R = str(input('você quer continuar?[S/N] \n')).upper()
