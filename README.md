# Curso de Python — lógica de programação e prática

Este repositório reúne os exercícios que desenvolvi durante meus estudos de **Python** no curso Técnico em Desenvolvimento de Sistemas. Ele registra minha evolução desde os fundamentos da linguagem até a resolução de problemas com listas, matrizes, funções, validação de dados e uma introdução ao desenvolvimento de APIs.

> Repositório de estudos em evolução: alguns arquivos representam exercícios concluídos e outros registram testes, revisões e etapas do meu aprendizado.

## Objetivo

Praticar lógica de programação, transformar regras de negócio em algoritmos e acompanhar minha evolução por meio de exercícios progressivos e pequenos projetos de console.

## Conteúdos estudados

### Fundamentos da linguagem

- Variáveis e tipos de dados
- Entrada e saída com `input()` e `print()`
- Conversão de valores com `int()` e `float()`
- Operadores aritméticos, relacionais e lógicos
- Formatação de textos com f-strings

### Controle de fluxo

- Estruturas condicionais com `if`, `elif` e `else`
- Estruturas de repetição com `for` e `while`
- Uso de `range()`, contadores e acumuladores
- Validação de dados e repetição de entradas inválidas
- Interrupção de laços com `break`

### Estruturas de dados

- Listas e listas paralelas
- Índices, fatiamento e percursos
- Métodos como `append()`, `insert()`, `remove()`, `pop()` e `sort()`
- Tuplas e o conceito de imutabilidade
- Conjuntos, diferenças e verificação de permissões
- Dicionários para representar dados estruturados
- Matrizes bidimensionais com laços aninhados

### Algoritmos e organização do código

- Criação e chamada de funções
- Parâmetros e valores de retorno
- Busca de valores e posições
- Identificação manual de maiores e menores valores
- Cálculo de soma, média e contagem
- Filtragem e transformação de listas
- Cópias de listas e matrizes com `copy` e `deepcopy`
- Ordenação com `sort()` e funções `lambda`
- Compreensões de listas

### Bibliotecas e desenvolvimento web

- Geração de números aleatórios com `random`
- Introdução ao FastAPI
- Criação de uma rota HTTP com resposta em JSON
- Execução de uma API local com Uvicorn

## Organização do repositório

```text
Curso-dev/
├── condicionais/   # decisões, notas, triângulos e jogos
├── estrutura/      # listas, tuplas, conjuntos e dicionários
├── função/         # exercícios com vetores, buscas, médias e funções
├── loops/          # repetições, acumuladores, Fibonacci e validações
├── matriz/         # matrizes 2x2 e 3x3, transposição e buscas
├── passaTempo/     # pequenos projetos e introdução ao FastAPI
├── provas/         # soluções da avaliação prática de lógica
├── revisao/        # exercícios integrando os conteúdos estudados
├── loja.py         # experimento de autenticação e dados de usuários
└── README.md
```

## Exercícios e projetos em destaque

### Condicionais e validações

- Cálculo e classificação de médias escolares
- Classificação de triângulos
- Jogo de pedra, papel e tesoura
- Simulação de análise de crédito
- Controle de acesso por cargo, horário e chave de emergência

### Laços e vetores

- Sequência de Fibonacci e tabuadas
- Busca e contagem de números em listas
- Inversão, ordenação e transformação de vetores
- Substituição e filtragem de valores
- Registro de vendas, descontos e total acumulado
- Jogo de adivinhação com números aleatórios

### Matrizes

- Leitura e exibição de matrizes 2x2 e 3x3
- Soma e média dos elementos
- Busca de valores e coordenadas
- Multiplicação por um valor escalar
- Transposição de matriz
- Verificação de quadrado mágico
- Substituição de elementos a partir de um limiar

### Estruturas de dados aplicadas

- Fila de tarefas com listas
- Configuração de banco de dados com tuplas
- Controle de permissões com conjuntos
- Cadastro de candidatos com listas e dicionários
- Controle de estoque com listas paralelas

### Avaliação prática de lógica

Os cinco programas da pasta `provas` aplicam os principais conceitos estudados:

1. Lista de números, média aritmética e contagem de pares.
2. Separação de pares e ímpares com multiplicação por escalar.
3. Transformação de uma matriz 3x3 com base em um limiar.
4. Auditoria do consumo energético de máquinas.
5. Monitoramento térmico de racks e sensores.

### Primeira API

O arquivo `passaTempo/api.py` utiliza FastAPI para disponibilizar uma rota simples que retorna uma resposta em JSON.

## Como executar

### Requisitos

- Python 3 instalado
- FastAPI e Uvicorn apenas para o exercício de API

Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/Matheus1807/Curso-dev.git
cd Curso-dev
```

Execute um exercício informando o caminho do arquivo. Exemplos:

```bash
python condicionais/jogo.py
python loops/Fibonacci.py
python matriz/3x3.py
python provas/5.py
```

Para executar a API:

```bash
python -m pip install fastapi uvicorn
python -m uvicorn passaTempo.api:app --reload
```

Depois, acesse `http://127.0.0.1:8000` no navegador.

## Próximos passos

- Aprimorar a divisão dos programas em funções reutilizáveis
- Adicionar tratamento de exceções para entradas inválidas
- Padronizar o código seguindo as recomendações da PEP 8
- Criar testes automatizados
- Organizar as dependências do projeto
- Expandir a API com novas rotas e operações CRUD
- Estudar programação orientada a objetos e bancos de dados

## Tecnologias

- Python 3
- FastAPI
- Uvicorn
- Git e GitHub

---

Desenvolvido para fins de estudo e prática de programação.
