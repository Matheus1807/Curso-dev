# Construa um programa que receba 8 números inteiros e os guarde em um vetor. Em
# seguida, crie um segundo vetor de mesmo tamanho no qual os números ímpares do
# vetor original sejam multiplicados por 2 e os números pares permaneçam
# inalterados. Ao final, exiba os dois vetores.
import copy
lista1 = []


for i in range(8):
    numero = int(input("Digite seu número: "))
    lista1.append(numero)

soma = 0
lista2 = copy.deepcopy(lista1)
for i in range(len(lista2)):
    if (lista2[i]%2 != 0):
        lista2[i] = lista2[i] * 2

print(lista2)