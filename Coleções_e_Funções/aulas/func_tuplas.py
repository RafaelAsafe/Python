""" demonstração de funções aplicaveis em tuplas"""

lanche = 'hamburguer', 'suco', 'pudim', 'pizza'  # tuplas são imutavéis
print(lanche)
# for i in lanche:
# print(f'eu vou comer {i}')
# for cont in range (0, len(lanche)):
# print('vou comer {}'.format(lanche[cont]))
# ou (f'vou comer {lanche[cont]}')


# enumerate mostra os itens e posição do elemento

for p, i in enumerate(lanche):
    print(f'Eu vou comer {i} na posicao {p}')
print(list(enumerate(lanche)))


# len mostra a quantidade de itens presente na tupla

print(len(lanche))

# soma de duplas

a = 1, 2, 3, 3
b = 4, 5, 6
c = a + b  # b+a é diferente de a+b
print(c)

# count conta quantas vezes certos caracteres aparecem na tupla

print(c.count(3))

# index mostra em que posção o objeto buscado esta,
# ele capta a primeira ocorrência

print(c.index(3))

# único modo de mudar uma tupla é apagar uma tupla inteira
