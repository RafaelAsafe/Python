lista=('hq',5.50,'graphic novel',25.00,'livro',20.00,'action figure',75.00)
print('*'*40)
print(f'{"lista de materiais":^40}')
print('*'*40)
for i in range(0,len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'{lista[i]:.>10.2f}')
print('*'*40)
