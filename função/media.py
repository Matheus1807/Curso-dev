# 7. Construa uma página onde o usuário digitará o nome e a média de cinco
# alunos e o programa só aceitará a média do aluno caso ela esteja entre zero
# e dez.

medias = []

for i in range(0,3):
    nome = input("Diga o nome")
    media = float(input("Digite a media: "))
    while (media < 0) or (media > 10):
        print('media errada!')
        media = float(input("Digite a media: "))
    medias.append([nome, media])