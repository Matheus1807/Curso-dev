# Construa um programa que o usuário digitará o nome e a idade de dez
# pessoas e o programa escreverá o nome do usuário mais novo.

lista = []

for i in range(3):
    nome = input(
        "Diga o nome: ")
    idade = int(input
        ("Diga a idade: "))
    lista.append(
        [nome , idade])

# Primeira forma
# mais_novo = 0 #indice

# for i in range(1, len(lista)):
#     if lista[i][1] < lista[mais_novo][1]:
#         mais_novo = i
# print(f'O mais novo é {lista[mais_novo][0]}')

# Segunda forma 
mais_novo = min(lista, key=lambda pessoa: pessoa[1])
print(f'o mais novo é {mais_novo[0]} e a idade dele é {mais_novo[1]} anos')