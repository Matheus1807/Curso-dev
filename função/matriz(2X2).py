# Construa uma matriz 2X2 e, como saída desse programa, a média e a soma
# dos valores digitados deverão ser calculadas.

matriz = []

# [i] é a linha e o [J] é a coluna
for i in range(2):
    for j in range(2):
        matriz[i][j] = int(input("Diga o numero: "))

soma = 0
for linha in matriz:
    for coluna in linha:
        soma += coluna