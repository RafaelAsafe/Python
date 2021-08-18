"exercício 78"
l = []
for i in range(0, 5):
    l.append(int(input('insira um valor na lista:')))
print('a lista é', l)
print(f'o maior valor da lista foi {max(l)}')
print(f'o menor valor da lista foi {min(l)}')

for i, p in enumerate(l):
    if p == max(l):
        print(f'O maior numero se encontra na posição {i}')
    elif p == min(l):
        print(f'O menor numero se encontra na posição {i}')
