# Desenvolva um módulo de console para auditar o consumo de combustível de
# # veículos que retornam à base operacional ao longo de um turno de trabalho.
# Restrição Técnica: O processamento deve utilizar unicamente
# acumuladores e variáveis numéricas primitivas (float e int), sem o uso de
# listas ou estruturas compostas.
carro = 0
media = 0
kmsT = 0

while True:
    user = input("Deseja continuar a auditoria? [nao ou sim]").lower()

    if user == 'nao' or user == 'n':
        print("Expediente encerrado!")
        break

    kms = float(input("Digite os kms pecorridos"))

    while kms < 0:
        kms = float(input("Digite o digite os metros pecorridos corretamente!"))
    
    combustivel = float(input("Digite os combust0ivel consumido"))

    while combustivel <= 0:
        print("Digite o combustivel sendo maior que 0!")
        combustivel = float(input("Digite os combustivel consumido"))

    consumo = kms/combustivel

    if consumo >= 12.0:
        print('Econômico')

    elif consumo >= 9 and consumo < 12:
        print('Padrão')

    else:
        print('Alto Consumo')

    media += consumo
    kmsT += kms
    carro += 1

print(f"Total de carros atendidos! {carro}\n"
      f"Total de kms percorridos - {kmsT}\n"
      f"Total de kml - {media}")

