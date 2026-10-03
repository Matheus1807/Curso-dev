# Construa um programa que peça ao usuário para digitar oito números e os guarde em um
# vetor. Depois, o programa deve pedir um número adicional e informar se esse número está
# presente no vetor. Se estiver, informe em qual posição (índice) ele foi encontrado pela
# # primeira vez.

# Meu vetor se chamará numeros
numeros = []

for i in range(3):
    numero = int(input("Digite seu número: "))
    numeros.append(numero)

num_adicional = int(input("Diga um número adicional: "))

if num_adicional in numeros:
    indice = numeros.index(num_adicional)
    print(f'{indice+1}')

else:
    print("Nao está na lista")

# for num in numeros :
#     if num == num_adicional
#     print(indice)