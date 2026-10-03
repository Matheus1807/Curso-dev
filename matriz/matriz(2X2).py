# Construa uma matriz 2X2 e, como saída desse programa, a média e a soma
# dos valores digitados deverão ser calculadas.


matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input('Digite um número: ')))
    matriz.append(linha)

soma = 0
for linha in matriz:
    for coluna in linha:
        soma += coluna

print(f'{matriz}')