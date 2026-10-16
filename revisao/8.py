# Construa um sistema de controle de reposição para almoxarifado utilizando vetores
# unidimensionais para gerenciar 6 itens industriais.
# Restrição Técnica: Utilize laços de repetição (for ou while) com controle de
# índices para percorrer as listas de forma sincronizada.
# O programa deve preencher duas listas paralelas de tamanho fixo (6
# posições): uma contendo o código numérico de cada produto e outra
# contendo o respectivo saldo em estoque.

codigo_numerico = []
estoque = []

for i in range(6):
    codigo = int(input('Digite seu codigo númererico '))
    saldo = float(input('Digite seu codigo númererico '))

    codigo_numerico.append(codigo)
    estoque.append(saldo)

# 2. Solicite ao operador o valor do "Estoque Mínimo de Segurança" 
# (um número inteiro único para a verificação de toda a linha).

estoque_minimo = int(input('Digite seu codigo númererico '))

# Realize uma varredura nas estruturas e identifique:
indice_menor = 0
indice_maior = 0
menor_saldo = estoque[0]
maior_saldo = estoque[0]

for i in range(6):
# ■ Quais produtos estão com saldo estritamente abaixo do estoque
# mínimo, exibindo seu código e quantidade atual;
    if estoque[i] < estoque_minimo:
        print(f'Código {codigo_numerico[i]} - Saldo Atual {estoque_minimo[i]}')

    # achar o maior
    if estoque[i] > estoque[indice_maior]:
        indice_maior = i

    else:
        indice_menor = i

# ■ O código e a quantidade do item que possui o menor saldo
# absoluto no almoxarifado;
# ■ O código e a quantidade do item com maior saldo absoluto.

