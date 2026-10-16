# Preenche a matriz 3x3 com as temperaturas dos sensores.
temperaturas = []

for rack in range(3):
    linha = []
    for sensor in range(3):
        temperatura = float(
            input(f'Digite a temperatura do Rack {rack}, Sensor {sensor}: ')
        )

        while temperatura < 10.0 or temperatura > 90.0:
            print('A temperatura deve estar entre 10.0°C e 90.0°C.')
            temperatura = float(
                input(f'Digite novamente a temperatura do Rack {rack}, Sensor {sensor}: ')
            )

        linha.append(temperatura)
    temperaturas.append(linha)

# Calcula a média de cada rack e encontra o ponto de maior temperatura.
maior_temperatura = temperaturas[0][0]
rack_maior = 0
sensor_maior = 0

print('\nTemperatura média de cada rack:')
for rack in range(3):
    soma_temperaturas = 0

    for sensor in range(3):
        temperatura = temperaturas[rack][sensor]
        soma_temperaturas += temperatura

        if temperatura > maior_temperatura:
            maior_temperatura = temperatura
            rack_maior = rack
            sensor_maior = sensor

    media_rack = soma_temperaturas / 3
    print(f'Rack {rack}: {media_rack:.2f}°C')

print('\nMatriz de temperaturas:')
for rack in range(3):
    for sensor in range(3):
        print(f'{temperaturas[rack][sensor]:8.2f}', end='')
    print()

print('\nPonto crítico da estrutura:')
print(f'Temperatura: {maior_temperatura:.2f}°C')
print(f'Localização: Rack {rack_maior}, Sensor {sensor_maior}')

if maior_temperatura >= 75.0:
    print('ALERTA: Ponto Crítico de Sobreaquecimento Detectado')
