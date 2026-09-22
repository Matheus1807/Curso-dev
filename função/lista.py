list = []
carros = ['Ferrari f430', 'Uno com escada', 'Civic g9', 'Opala', 'Golf']

# fala o tipo
print(type(carros))

# printa o carro da posição 4 de 0 a 4
print(carros[4])

# slice = corte, para pegar apenas de um carro a outro 
carro_quesaiu = carros.pop()
print(f"carro = {carro_quesaiu}")

i = 0
# Imprimir elemento por elemento
for carro in carros:
    print(f'{carro}')

# # com o len ele vai verficar cada posição que tem na lista e vai criar organizada
# # e com cada modificação na lista ele ja muda automaticamente o tamanho
for i in range(len(carros)):
    print(f'{i+1} - {carros[i]}')


# Retornar as notas
# list
# notas = [2,3,4.5,6,7,8, 'E AE']
# for nota in notas:
#     print(type(nota), nota)
