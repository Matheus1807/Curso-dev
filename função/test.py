lista = []

for i in range(2):
    aluno = input("Nome do aluno: ")
    nota = float(input('Digite a nota: '))
    lista.append([aluno, nota])

for i in range(len(lista)):
    if lista[i][1] >= 6:
        print(f'Os alunos aprovados são {lista[0]}')