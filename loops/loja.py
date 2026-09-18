# 1. Desenvolva um programa para registrar as vendas de uma loja ao longo
# do dia. O programa deve processar múltiplos clientes até que o
# operador digite 0 no total de compras para encerrar o expediente.
cliente =  0
total_vendas = 0

while True:

    venda = float(input(
    "Digite o valor da venda em R$ ou digite 0 para encerrar o expediente: "
    ))
    cupons = float(input(
    "Digite o valor do desconto: "
    ))

    if venda == 0:
        print("Expediente encerrado!")
        break

    while venda < 0:
        print("Erro na digitação!")
        venda = float(input(
     "Digite o valor da venda em R$ ou digite 0 para encerrar o expediente: "
    ))
    while cupons < 0:
        print("Erro na digitação!")
        cupons = float(input(
        "Digite o valor do desconto: "
        ))

    
    cupons = venda * (cupons / 100)
    venda_final = venda - cupons
    total_vendas += venda_final
    cliente += 1

    print(f'Venda final - {venda_final}')
    print(f'Total vendas- {total_vendas}')

print(f'Total vendas- {total_vendas}')
print(f'Total clientes- {cliente}')