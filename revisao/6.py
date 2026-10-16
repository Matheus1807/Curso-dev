# Desenvolva um programa que solicite o preenchimento de uma matriz 3 × 3 com
# números inteiros e, em seguida, peça ao usuário um valor numérico constante
# (escalar). Utilizando laços de repetição aninhados, o programa deve multiplicar cada
# elemento da matriz original por esse valor escalar e exibir a matriz resultante
# formatada em linhas e colunas.

# import copy

# matriz = []

# for i in range(3):
#     linha = []
#     for j in range(3):
#         num = int(input('Digite um número: '))
#         linha.append(num)
#     matriz.append(linha)

# print(matriz)

# matriz2 = copy.deepcopy(matriz)

# escalar = int(input('Digite um multiplicador constante'))
# posicao = 0

# for linha in matriz2:
#     for numero in linha:
#         posicao=linha.index(numero)
#         numero=numero*escalar
#         linha[posicao]=numero

# print(matriz2)

import copy

def criar_matriz():
    matriz = [] 
    for i in range(3):
        linha = []
        for j in range(3):
            num = int(input('Digite um número: '))
            linha.append(num)
        matriz.append(linha)
    print(matriz)

def multiplicar_matriz (matriz,escalar):
    matriz2 = copy.deepcopy(matriz)
    for linha in matriz2:
        for numero in linha:
            posicao=linha.index(numero)
            numero=numero*escalar
            linha[posicao]=numero


matriz = criar_matriz()

print("Matriz original:", matriz)

escalar = int(input("Digite um multiplicador constante: "))

matriz2 = multiplicar_matriz(matriz, escalar)

print("Matriz multiplicada:", matriz2)