"""Funções Aula 20 """
# funções são metodos editáveis, por meio deles é possível reduzir o corpo do codigo e reutilizar partes do código.
# isso pode ser feito sem parametro,ou seja sem utilizar informações do código


def som(*num):
    s = 0
    for v in num:
        s = s + v
    print(f'a soma desses valores é: {s} \n')


def soma(a, b):
    s = a + b
    print(f'o valor da soma é {s}')


def linha():
    print('*' * 50)
#  Ou com parametro de referencia


def moldura(msg):
    print('*' * 30)
    print(msg)
    print('*' * 30)


linha()
print('olá mundo')
linha()

#  Ou com parametro de referencia


moldura('Olá mundo')

# as funções normalmente são limitadas pelos parametros

soma(2, 3)
# caso for inserido (2,3,4), irá dar erro
# para ter a possíbilidade de parametros variaveis usa-se empacotamento.

som(1, 2, 3, 4, 5)
som(1, 2, 3)
som(12, 15, 17)

# essa função transformar as variáveis em tuplas(logo pode-se se usar as ferramentas para lidar com tuplas)
