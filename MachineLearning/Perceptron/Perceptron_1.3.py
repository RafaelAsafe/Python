# def step_ativation
"""
Modelo matématico para perceptron, os pesos não foram automatizados para fins educacionais.

"""
import numpy as np   # biblioteca para manipulação de matemática em C (mais rápida)
import pandas as pd  # biblioteca para manipulação de dados

# importar csv com inputs e saidas desejadas de um arquivo csv

dataframe = pd.read_csv("C:\Tarefa_INART_10\iris_data.csv")

colunas_dt = np.size(dataframe['x1'])

# estabelecer dados iniciais
x1 = np.array(dataframe['x1'])  # entrada 1
x2 = np.array(dataframe['x2'])  # entrada 2
x3 = np.array(dataframe['x3'])  # entrada 3
x4 = np.array(dataframe['x4'])  # entrada 4
d = np.array(dataframe['d'])  # saidas desejadas
# vetor de zeros para as saidas do algoritmo de treino
y = np.zeros(colunas_dt)
# Vetor de pesos iniciado com numeros aleatorios
W = np.random.rand(5)

# estabelecer taxa de aprendizagem
n = 0.1

# estabelecer contador de épocas
epoca = 0

# aprendizado
error = True
while error:
    error = False
    for i in range(colunas_dt):

        # calculo de y

        if((x4[i]*W[4])+(x3[i]*W[3])+(x2[i]*W[2])+(x1[i]*W[1])+(W[0]*-1)) > 0:
            y[i] = 1
        else:
            y[i] = 0

        # comparação do y obtido com o y desejado
        for i in range(colunas_dt):
            if y[i] != d[i]:

                # atualização dos pesos
                W[0] += n*(d[i]-y[i])*-1
                W[1] += n*(d[i]-y[i])*x1[i]
                W[2] += n*(d[i]-y[i])*x2[i]
                W[3] += n*(d[i]-y[i])*x3[i]
                W[4] += n*(d[i]-y[i])*x4[i]
                print(f'o peso de x0: {W[0]}')
                print(f'o peso de x1: {W[1]}')
                print(f'o peso de x2: {W[2]}')
                print(f'o peso de x3: {W[3]}')
                print(f'o peso de x4: {W[4]}')
                print(f'epocas: {epoca}')

                epoca += 1
                error = True

print(f'o peso de x0 final: {W[0]}')
print(f'o peso de x1 final: {W[1]}')
print(f'o peso de x2 final: {W[2]}')
print(f'o peso de x3 final: {W[3]}')
print(f'o peso de x4 final: {W[4]}')
print(f'epocas final:{epoca}')

while True:
    teste_x1 = float(input('\ninsira um x1 \n'))
    teste_x2 = float(input('insira um x2 \n'))
    teste_x3 = float(input('insira um x3 \n'))
    teste_x4 = float(input('insira um x4 \n'))
    if((teste_x4*W[4])+(teste_x3*W[3])+(teste_x2*W[2])+(teste_x1*W[1])+(W[0]*-1)) > 0:
        teste_y = 1
    else:
        teste_y = 0
    if teste_y == 1:
        print(f'Para estes valores o espécime é iris-setoza \n')
    else:
        print(f'Para estes valores o espécime é iris-versicolor \n')
    GoOn = input('Gostaria de continuar o teste? [s/n] \n')
    if GoOn in ('nN'):
        break
