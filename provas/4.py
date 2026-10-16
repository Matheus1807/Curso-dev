# Armazena os códigos e os consumos em duas listas paralelas.
codigos = []
consumos = []

for i in range(5):
    codigo = int(input(f'Digite o código da máquina {i + 1}: '))
    consumo = float(input(f'Digite o consumo da máquina {codigo} em kWh: '))

    while consumo <= 0:
        print('O consumo deve ser maior que zero.')
        consumo = float(input(f'Digite novamente o consumo da máquina {codigo}: '))

    codigos.append(codigo)
    consumos.append(consumo)

teto_operacional = float(input('Digite o Teto Operacional de Consumo em kWh: '))

# Percorre as listas com índices para calcular todos os resultados.
soma_consumos = 0
indice_maior_consumo = 0
quantidade_acima_teto = 0

print('\nMáquinas acima do teto operacional:')
for i in range(5):
    soma_consumos += consumos[i]

    if consumos[i] > consumos[indice_maior_consumo]:
        indice_maior_consumo = i

    if consumos[i] > teto_operacional:
        quantidade_acima_teto += 1
        print(f'Código: {codigos[i]} | Consumo: {consumos[i]:.2f} kWh')

if quantidade_acima_teto == 0:
    print('Operação Dentro dos Parâmetros de Eficiência')

media_consumo = soma_consumos / 5

print('\nMáquina com o maior consumo:')
print(f'Código: {codigos[indice_maior_consumo]}')
print(f'Consumo: {consumos[indice_maior_consumo]:.2f} kWh')
print(f'Média de consumo: {media_consumo:.2f} kWh')
