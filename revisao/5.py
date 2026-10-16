# Exercício 5: Contagem de Valores Menores que um Limiar em Matriz
# Retangular
# Desenvolva um programa que leia os valores de uma matriz 2 × 4 de números
# inteiros. O programa deve contar quantos valores estão abaixo de um limiar, que
# também será informado pelo usuário, estão presentes na estrutura e exibir a
# contagem total, além de imprimir a matriz completa formatada em linhas e colunas.
# limiar = numero adicional para pecorrer na matriz


matriz = []

for i in range(2):
    linha = []
    for j in range(4):
        numero = int(input("Digite seu número"))
        linha.append(numero)
    matriz.append(linha)

limiar = int(input("Digite o limiar"))
contador = 0

for i in matriz:
    for numero in i:
        if numero < limiar:
            contador += 1

print(f'Existe(m) {contador} números(s) menor(es) do que \
      limiar {limiar} na matriz abaixo')