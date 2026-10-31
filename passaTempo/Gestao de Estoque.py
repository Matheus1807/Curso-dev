# 1. Sistema de gestão de estoque e vendas
# um sistema para lojas pequenas com cadastro de produtos
# atualização de estoque, vendas, descontos 
# e relatórios de faturamento.
# Praticar dicionários, listas, funções, loops e cálculos.

estoques_geral = []
usuarios = []

while True:

    pergunta1 = input(
        'Deseja continuar o expediente? [s] ou [n]: '
    ).lower().strip()

    if pergunta1 == 'n' or pergunta1 == 'nao':
        break

    # CADASTRO
    pergunta2 = input(
        'Deseja adicionar algum produto novo? [s] ou [n]: '
    ).lower().strip()

    if pergunta2 == 's' or pergunta2 == 'sim':
        produto_novo = input(
            'Digite o nome do produto novo: '
        ).lower().strip()

        estoque_produto = int(input(
            'Digite o estoque: '
        ))

        while estoque_produto < 0:
            print('Valor digitado do estoque errado!')
            estoque_produto = int(input(
                'Digite o estoque: '
            ))

        produtos_estoques = {
            'nome': produto_novo,
            'estoque': estoque_produto,
        }

        estoques_geral.append(produtos_estoques)
        print('Produto cadastrado com sucesso!')

    # VENDAS
    resposta_venda = input(
        'Vendeu algum produto? [s] ou [n]: '
    ).lower().strip()

    if resposta_venda == 'sim' or resposta_venda == 's':
        produto_vendido = input(
            'Qual foi o produto vendido? '
        ).lower().strip()

        encontrado = False

        for produto in estoques_geral:
            if produto_vendido == produto['nome']:
                encontrado = True

                vendas = int(input(
                    'Quantas unidades foram vendidas? '
                ))

                if vendas > 0 and vendas <= produto['estoque']:
                    produto['estoque'] -= vendas

                    print('Venda registrada com sucesso!')
                    print(produto)
                else:
                    print('Quantidade inválida ou estoque insuficiente!')

                break

        if encontrado == False:
            print('Produto não encontrado!')

    print('\nEstoque atual:', estoques_geral)

print('\nExpediente encerrado!')
print('Estoque final:', estoques_geral)
    