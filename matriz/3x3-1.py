# Tendo uma matriz numérica 3x3:
# ◆ substitua múltiplos de 3 por Fus;
# ◆ substitua múltiplos de 5 por Ro;
# ◆ substitua múltiplos de 3 e de 5 por Dah.

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        numero = float(input("Digite o número: "))
        if (numero %3 == 0) and (numero %5 == 0):
            numero = "Dah"
        elif( numero%3 == 0):
            numero = "Fus"
        elif (numero%5 == 0):
            numero = "Ro"
            linha.append(numero)
        linha.append(numero)
    matriz.append(linha)

for linha in matriz:
    for numero in linha:
        print(f'Seu número é: {numero}')

