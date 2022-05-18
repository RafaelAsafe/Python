"Dicionário Aula 19"
# Um dicionário é uma estrutura semelhante as listas mas seus indices podem ser
# alterados
# o indice é chamodo de key e o conteúdo de value
# para declara um dicionario usar:
dicio = {}
# ou
dici = dict()
# para inserir dados inicais, a primeira string no exeplo abaixo representa a key e a segunda o value:
# para acessar os valoes usar os metodos internos abaixo:
dicio = {'nome': 'raquel', 'idade': 22}
print(dicio)
print(dicio['nome'])
print(dicio.values())
print(dicio.keys())
# acessar um value especifico,digitando a key:
print(dicio['nome'])
print(
    f'A pessoa tem o nome de {dicio["nome"]} e sua idade é {dicio["idade"]} \n ')
# acessar o itens do dicionario
print(f'{dicio.items()}\n')
# acessar partes do dicionario por meio de estrutura de repetição (não possuímos enumerate em dicionarios)
for k in dicio.keys():
    print(k)
    print()
for k, v in dicio.items():
    print(f'{k}={v}')
# adicionar valores ou alterar valores:
dicio['genero'] = 'F'
dicio['nome'] = 'berta'
print(dicio)
# deletar keys ou values
del dicio['genero']
# é possivel realisar fazer listas de dicionarios pelo comando append
