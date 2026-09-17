# for range, ali ele vai gerar quatro posições a partir do zero até o 3 e pulando de 1 em 1
# lista = ['sorvete', 'carro']
# for elemento in lista:
#     print(elemento)
# vai printar a lista: sorverte embaixo carro

# range (0, 4) -> [0, 1, 2, 3] - [4] sendo o numero limite ou seja vai de 0 a 3 - [0] aonde começa
# for i in range(0,4,2):
#     print(i)

# 
numero = int(input("Numero "))
for i in range(0, 10):
    resultado = numero * (i + 1)
    print(f'{numero} * {i + 1} = {resultado}')
