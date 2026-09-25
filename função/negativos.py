lista = []
for i in range(0,10):
    numero = int(input("Digite seu número"))
    lista.append(numero)

for numero in lista:
    if (numero < 0):
        # lista.index(numero[, start[, end]])
        indicePosicao = lista.index(numero)
        lista.remove(numero)
        numero = 0
        lista.insert(indicePosicao, numero)


print(lista)