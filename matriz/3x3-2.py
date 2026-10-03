matriz = []
pos_i = 0
pos_j = 0
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input("Digite seu número: "))
        linha.append(num)
    matriz.append(linha)

maior = max(max(matriz))

for linha in matriz:
    for numero in linha:
        if numero == maior:
            pos_i = matriz.index(numero)
            pos_j = linha.index(numero)


print(f'O maior é {maior}, linha é: {pos_i}, coluna é {pos_j}')