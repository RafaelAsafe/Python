# def step_ativation
"""
Modelo matématico para perceptron, os pesos não foram automatizados para fins educacionais.

"""
import numpy as np
# biblioteca para manipulação de matemática em C (mais rápida)
import pandas as pd  # biblioteca para manipulação de dados

# importar csv com inputs e saidas desejadas de um arquivo csv

dataframe = pd.read_csv("Python\MachiningLearning\SVM\AND.csv")

colunas_dt = np.size(dataframe['x1'])

# estabelecer dados iniciais

x = np.delete(dataframe, -1, axis=1)  # entrada 1
d = (dataframe[:, -1])  # saidas desejadas
# vetor de zeros para as saidas do algoritmo de treino
y = np.zeros(colunas_dt)
# Vetor de pesos iniciado com numeros aleatorios
W = np.random.rand(len(x[0]))
bias = W[0]*-1

# estabelecer taxa de aprendizagem
n = 0.2

# estabelecer contador de épocas
epoca = 0

# aprendizado
error = True
while error:
    error = False
    for i in range(len(x)):

        # calculo de y

        if (sum(x[i]*W) + bias) > 0:
            y = 1
        else:
            y = 0

        # comparação do y obtido com o y desejado
        if y != d[i]:
            # atualização dos pesos
            W += n*(d[i]-y)*x[i]
            print(f'o peso de x{i}: {W[i]}')
            print(f'epocas: {epoca}')

            error = True
        epoca += 1

for i in len(x[0]):
    print(f'o peso de final x{i}: {W[i]}')
print(f'epocas final:{epoca}  ')

while True:
    teste_x1 = int(input('\ninsira um x1 \n'))
    teste_x2 = int(input('insira um x2 \n'))
    if(sum(x[i]*W) + bias) > 0:
        teste_y = 1
    else:
        teste_y = 0
    print(f'Para estes valores y é igual a {teste_y} \n')
    GoOn = input('Gostaria de continuar o teste? [s/n] \n')
    if GoOn in ('nN'):
        break
