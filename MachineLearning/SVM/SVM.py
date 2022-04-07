import matplotlib.pyplot  # biblioteca responsável pelos gráficos
import random  # biblioteca responsável por numeros aleatórios

# funções


def passo1(arquivo):
    arq = open(arquivo, "r")
    k = sum(1 for linha in arq)
    arq.close()
    return k

# -------------------x--------------------------
# algoritmo de treinamento perceptron


arq = open('bancodedados.txt', 'r')
k = passo1('bancodedados.txt')

# Passo 1-número de amostras de treinamento

y = []
a = []
l = []
d = []

# Passo 2-obter saida desejada para cada amostra

txt = arq.readlines()
for i in txt:
    s = i.split()
    a.append(int(s[0]))
    l.append(int(s[1]))
    d.append(int(s[2]))
    y.append(int(0))

# passo 3-vetor de pesos com números aleatórios

w1 = 0.5
w2 = 0.5
w0 = 0.5

# passo 4-taxa de aprendizado

n = 0.5

# passo 5-número de épocas

epoca = 0
error = True
while error == True:
    error = False
    for i in range(k):

        # calculo de y

        if((a[i]*w1)+(l[i]*w2)+(w0*-1)) >= 0:
            y[i] = 1
        else:
            y[i] = 0
    for i in range(k):
        if y[i] != d[i]:

            # comparação do y obtido com o y desejado

            epoca += 1

            # atualização dos pesos

            w1 += n*(d[i]-y[i])*a[i]
            w2 += n*(d[i]-y[i])*l[i]
            w0 += n*(d[i]-y[i])*-1
            error = True
            print('o peso de a: ', w1)
            print('o peso de l: ', w2)
            print('o peso de b: ', w0)
            print('epocas: ', epoca)


print('o peso de a final: ', w1)
print('o peso de l final: ', w2)
print('o peso de b final: ', w0)
print('epocas final: ', epoca)
arq.close()
