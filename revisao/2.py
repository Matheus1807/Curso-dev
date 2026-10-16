# Construa um programa que leia 10 números inteiros, armazene-os em uma lista e,
# em seguida, solicite um número adicional para consulta. O sistema deve verificar e
# exibir se esse valor está presente no vetor e a quantidade exata de vezes que ele se
# repete.

lista = []
    
for i in range(10):
    numero = int(input("Digite seu número"))
    lista.append(numero)

contador = 0
num = int(input('Digite seu número adicional: '))
for numero in lista:
    if numero == num: 
        contador += 1
print(f'Numero encontrado {contador} vezes')
    
# Outra forma

# lista = []

# for i in range(3):
#     numero = int(input("Digite seu número"))
#     lista.append(numero)

# num_adicional = int(input("Diga um número adicional: "))

# for i in range(len(lista)):
#     if num_adicional in lista:
#         indice = lista.index(num_adicional)
#         print(f'{indice+1}')