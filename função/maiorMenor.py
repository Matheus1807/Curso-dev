# Construa um programa onde o usuário digitará dez números inteiros. O programa deve
# identificar qual é o maior e qual é o menor número digitado, exibindo também a posição
# # (índice) em que cada um deles se encontra no vetor.

lista = []

for i in range(0, 10):
    numero = int(input('Digite o número: '))
    lista.append(numero)

maior = max(lista)
menor = min(lista)

for numero in lista:
    indice = lista.index(numero)