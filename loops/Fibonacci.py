anterior= 0
atual = 1
proximo = (anterior + atual)

while (atual <= 2000):
    anterior = atual
    atual = proximo
    proximo = (anterior + atual)
    print(f'Numero SEQ - {proximo}')