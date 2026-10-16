import copy

def matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(2):
            num = int(input('digite o numero: '))
            linha.append(num)
        matriz.append(linha)
    return(matriz)

def busca_elemento(matriz , maior):
    # for linha in matriz:
    #     for numero in linha:
    #         if numero > maior:
    #             print(numero)

    for i in range(len(matriz)):
        for j in range(3):
            if matriz[i][j] > maior:
                print(matriz[i][j])
                matriz[i][j] = 0
                print(matriz[i][j])


m = matriz()
m2 = copy.deepcopy(matriz())
maior = int(input('Digite um corte'))
print (matriz)
busca_elemento(m, maior)