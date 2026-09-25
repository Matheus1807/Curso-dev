# Construa um programa onde o usuário digitará cinco números para preencher um vetor. O
# programa deve criar um segundo vetor que contenha os mesmos elementos do primeiro,
# porém na ordem inversa, e exibir o novo vetor na tela.

lista1 = []

for i in range(0,5):
    num1 = int(input("Digite cinco números: "))
    lista1.append(num1)

lista2 = list(reversed(lista1))
print(lista2)