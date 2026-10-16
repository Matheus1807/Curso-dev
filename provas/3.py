# Preenche uma matriz 3x3 com números inteiros.
matriz = []

for linha in range(3):
    nova_linha = []
    for coluna in range(3):
        numero = int(input(f'Digite o valor [{linha}][{coluna}]: '))
        nova_linha.append(numero)
    matriz.append(nova_linha)

limiar = int(input('Digite o valor de corte (limiar): '))

# Cria uma nova matriz, substituindo por zero os valores acima do limiar.
matriz_resultante = []
quantidade_acima = 0

for linha in range(3):
    nova_linha = []
    for coluna in range(3):
        valor = matriz[linha][coluna]
        if valor > limiar:
            nova_linha.append(0)
            quantidade_acima += 1
        else:
            nova_linha.append(valor)
    matriz_resultante.append(nova_linha)

print(f'Quantidade de elementos acima do limiar: {quantidade_acima}')
print('Matriz resultante:')
for linha in matriz_resultante:
    for valor in linha:
        print(f'{valor:6}', end='')
    print()
