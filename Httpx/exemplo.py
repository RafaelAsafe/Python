def soma(*args):
    soma = 0
    for i in args:
        soma = soma + i

    return soma


resultado = soma(*[1, 2, 3, 4, 5, 6])
print(resultado)


lista = [1, 2]
a, b = lista
lista = 1,2,3,4

print(a, b)
print(lista)
