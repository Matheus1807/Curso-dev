# 6. Construa uma página/programa onde o usuário digitará o nome e o bairro de
# dez pessoas. O programa exibirá o nome e bairro das pessoas em ordem
# alfabética.

lista = []

for i in range(2):
    bairro = input("Nome do bairro: ")
    nome = input('Digite o nome: ')
    lista.append([bairro, nome])

lista.sort(key=lambda nome: nome[1])
# Na vida real usa o x no lugar do nome
# lista.sort(key=lambda x: x[1])

print(f'{lista[1]}')