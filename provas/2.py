# Lê 10 números inteiros e os armazena no vetor original.
vetor_original = []

for i in range(10):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))
    vetor_original.append(numero)

# Separa os valores em duas listas independentes.
pares = []
impares = []

for numero in vetor_original:
    if numero % 2 == 0:
        pares.append(numero * 3)
    else:
        impares.append(numero)

print(f'Vetor original: {vetor_original}')
print(f'Pares multiplicados por 3: {pares}')
print(f'Ímpares: {impares}')
print(f'Quantidade de elementos em pares: {len(pares)}')
print(f'Quantidade de elementos em ímpares: {len(impares)}')
