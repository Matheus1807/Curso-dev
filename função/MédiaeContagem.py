# Construa um programa onde o usuário digitará seis notas (números reais). O programa
# deve calcular a média dessas notas e, em seguida, exibir quantas e quais notas ficaram
# estritamente acima da média calculada.

notas = []

for i in range(0,6):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

# [sun] soma a minha lista [notas], [len] é o tamanho da lista [notas]  
media = sum(notas)/len(notas)
print(f'A sua média é: {media}')

acima_medidia = [nota for nota in notas if nota > media]
print('Nota acima da média!\n' ,
'Parabéns'
)

# outro tipo

# acima_media = []
# for nota in notas:
#     if nota >= media:
        # acima_media.append(nota)