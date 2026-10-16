def busca_elemento(matriz2 , numero):
    for linha in matriz2:
        for numero in linha:
            if numero > maior:
                print(numero)

m = matriz()
matriz2 = copy.deepcopy(matriz)
maior = int(input('Digite um corte'))
busca_elemento(m, maior)