# usuário digitará seis notas (números reais). 
# O programa deve calcular a média dessas notas e, 
# em seguida, exibir quantas e quais notas ficaram 
# estritamente acima da média calculada.

notas = []
for _ in range(0, 6):
    nota = float(input('Digite a nota: '))
    notas.append(nota)

# media
media = sum(notas)/len(notas)

# saber quem esta acima da media
# V1 -> pythones
acima_media = [nota for nota in notas if nota > media]
print(f'Qtd notas acima da média: {len(acima_media)}')
for nota in acima_media:
    print(nota)

# V2 -> 'normal'
acima_media = []
for nota in notas:
    if nota > media:
        acima_media.append(nota)