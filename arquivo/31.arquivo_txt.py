# escrever arquivo (como não existe, vai criar)

# modo 'w': cria ou sobrescreve o arquivo

with open('teste_txt.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Nome do Arquivo.\n')
    arquivo.write('Teste.\n')

with open('teste_txt.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('agora só adiciona.\n')

# leitura
# with open('teste_txt.txt', 'a+', encoding='utf-8') as arquivo:
#     # otimizado (ler linha por linha)
#     for linha in arquivo:
#         print(linha.strip())
0