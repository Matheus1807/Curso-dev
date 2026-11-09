import csv

try:
    with (open('banco.csv', "r", encoding='utf-8') as arquivo,
        open('pedidos_reposicao.csv', "w",  encoding='utf-8') as arquivo_reposicao):

        leitor = csv.DictReader(arquivo, delimiter=';')

        escritor = None

    try:
                for produto_alm in leitor:

                    estoque_minimo = int(produto_alm['estoque_minimo'])
                    saldo = int(produto_alm['saldo_atual'])
                    try:
                        if saldo < estoque_minimo:
                            
                            faltando = estoque_minimo - saldo

                            almoxarifado = {
                                'Id': produto_alm['id'],
                                'Nome do Produto': produto_alm['produto'],
                                'Saldo atual': saldo,
                                'Estoque minímo': estoque_minimo,
                                'Estoque faltando': faltando
                            }

                            if escritor == None:
                                cabecalhos = list(almoxarifado.keys())
                                escritor = csv.DictWriter(arquivo_reposicao, delimiter=';', fieldnames=cabecalhos)
                            # escrever a primeira linha (que são os nomes das colunas)
                                escritor.writeheader()
                            escritor.writerow(almoxarifado)
                    except ValueError:
                        print(f"Erro ao converter valores para inteiros na linha: {produto_alm}")
    except Exception as e:
                print(f"Ocorreu um erro durante a execução do programa: {e}")
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique se o arquivo 'banco.csv' está no diretório correto.")