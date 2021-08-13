"listas"
# listas são categorizadas pelos: []
lista = [2, 3, 4, 5]
# para modificalas usamos os seguintes comandos
# acrescentar valor a lista"
lista.append(8)
# *acrescentar valores em uma localização específica
lista.insert(0, 'olá')
# *criar uma lista utilizando range
valores = list(range(2, 10))
# *organizar as listas em ordem crescente
valores.sort()
# *ou em ordem decrescente
valores.sort(reverse=True)
# se quiser que a lista vá pulando de valor em valor fazer a formação(2,10,2) mesmo valor de range mais ele vai pulando de 2 em 2
# *saber a quantidade de elementos da lista
print(len(valores))
# *ligação entre uma lista e outra
a = [2, 3, 4, 5]
b = a
b.insert(2, 2)
print(f'lista a é {a}\nlista b é {b}')
# *fazer uma copia de uma lista para outra variavel
c = [2, 3, 4, 5]
d = c[:]
c[1] = 8
print(f'lista c é {c}\nlista d é {d}')
# *saber a quantidade de elementos da lista
print(len(valores))
# ligação entre uma lista e outra"
a = [2, 3, 4, 5]
b = a
b.insert(2, 2)
print(f'lista a é {a}\nlista b é {b}')
# *fazer uma copia de uma lista para outra variavel
c = [2, 3, 4, 5]
d = c[:]
c[1] = 8
print(f'lista c é {c}\nlista d é {d}')
# fazer uma lista composta, ou seja um lista de listas
listas = [a, b, c, d]
print(listas)
