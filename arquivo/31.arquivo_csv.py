import csv

dados = [
    {'marca': 'Ford', 'modelo': 'Ka Baratinha', 'ano': 1999},
    {'marca': 'Fiat', 'modelo': 'Palio', 'ano': 1997},
    {'marca': 'BYD', 'modelo': 'King', 'ano': 2025},
]

cabecalho = ['marca', 'modelo', 'ano']

# escrever um csv a partir do dicionario
with open('carros.csv', 'w', encoding='utf-8', 
          newline='') as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=cabecalho,
                              delimiter=';')
    # escritor = csv.writer(arquivo, delimiter=';')
    
    # primeiro escrevo o cabeçalho na primeira linha
    escritor.writeheader()

    # escrever os dados -> writerows() -> escreve varias linhas
    escritor.writerows(dados)
