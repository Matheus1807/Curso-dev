# Construa um programa onde o usuário digitará o nome e a média de dez
# alunos e o programa escreverá, na tela, o nome de todos com a média acima
# ou igual a seis.

lista = []

for i in range(0,2):
    aluno = input(
        'Digite o nome ')
    nota = int(input(
        'Digite a nota '))
    lista.append(
        [aluno , nota])

# for each
for aluno_nota in lista:
# o nome de todos com a média acima ou igual a seis. 
    if aluno_nota[1] >= 6:
        print(aluno_nota[0])

# range
# for i in range(0, len(lista)):
#     if lista[i][1]:
#         print(lista[i][0])