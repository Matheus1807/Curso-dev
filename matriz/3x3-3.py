# Pegue uma matriz 3x3 e gere uma nova matriz onde as linhas da original
# viram as colunas da nova.
import copy

matriz = []
nova_matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        num = int(input('Digite seu número: '))
        linha.append(num)
    matriz.append(linha)
nova_matriz = copy.deepcopy(matriz)

for i in range(3):
    for j in range(3):
       nova_matriz[j][i]   = matriz[i][j]

print(f'{matriz} \n',nova_matriz)