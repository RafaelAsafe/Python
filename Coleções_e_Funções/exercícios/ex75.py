tupl = (int(input('insira o primeiro valor ')), int(input('insira o segundo valor ')),
        int(input('insira o terceiro valor ')), int(input('insira o quarto valor ')))
x = 0
print(f'os numeros inseridos foram {tupl}')
print(f'o numero nove apareceu {tupl.count(9)} vezes')
if 3 in tupl:
    print(f'o número 3 apareceu na posição {tupl.index(3)+1}')
else:
    print('o valor 3 não aparece na tupla')
print(f'foram digitados estes números pares:')
for i in tupl:
    if i % 2 == 0:
        print(i)
