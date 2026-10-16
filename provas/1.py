# Solicita 6 números inteiros e os armazena em uma lista.
numeros = []

for i in range(6):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))
    numeros.append(numero)

# Calcula a média e conta os números pares.
soma = 0
quantidade_pares = 0

for numero in numeros:
    soma += numero
    if numero % 2 == 0:
        quantidade_pares += 1

media = soma / len(numeros)

print(f'Lista completa: {numeros}')
print(f'Média aritmética: {media:.2f}')
print(f'Total de números pares: {quantidade_pares}')
