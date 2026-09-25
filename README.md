# Curso de Python — exercícios e evolução

Este repositório reúne os exercícios que desenvolvi durante meus estudos de **Python**. Os programas registram minha evolução desde os fundamentos da linguagem até pequenos projetos com validação de dados, jogos e uma introdução à criação de APIs.

> Projeto em desenvolvimento: novos exercícios serão adicionados conforme avanço no curso.

## Conteúdos estudados

- Variáveis e tipos de dados
- Entrada e saída com `input()` e `print()`
- Conversão de valores com `int()` e `float()`
- Operadores matemáticos, relacionais e lógicos
- Estruturas condicionais com `if`, `elif` e `else`
- Estruturas de repetição com `for` e `while`
- Listas, índices, fatiamento, `append()`, `pop()` e `len()`
- `range()` e operador `in`
- Validação de dados informados pelo usuário
- Formatação de textos com f-strings
- Uso do módulo `random`
- Introdução ao FastAPI e criação de rotas

## Organização do repositório

```text
Curso-dev/
├── condicionais/
│   ├── curso.py           # médias escolares e validação de notas
│   ├── ex4.py             # classificação de triângulos
│   └── jogo.py            # pedra, papel e tesoura
├── função/
│   ├── ex10-a.py          # leitura e armazenamento de números
│   ├── lista.py           # índices, remoção e percurso de listas
│   └── maquinário.py      # controle de acesso com listas e condições
├── loops/
│   ├── Fibonacci.py       # sequência de Fibonacci
│   ├── for.py             # tabuada com for e range
│   ├── loja.py            # registro de vendas e descontos
│   ├── notasLoops.py      # validação de notas com while
│   └── numAleatorio.py    # jogo de adivinhação com números aleatórios
└── passaTempo/
    ├── api.py             # primeira API com FastAPI
    └── emprestimo.py      # simulação de análise de crédito
```

## Exercícios em destaque

### Calculadora de médias escolares

Recebe notas, valida valores entre `0` e `10` e calcula médias escolares, indicando a situação do aluno.

### Jogo de pedra, papel e tesoura

Utiliza o módulo `random` para criar a escolha do computador e estruturas condicionais para determinar o resultado.

### Jogo de adivinhação

Gera números aleatórios e permite várias tentativas, praticando contadores, laços e condições.

### Registro de vendas

Processa vários clientes, aplica descontos e acumula o total vendido até o encerramento do expediente.

### Prática com listas

Explora acesso por índice, remoção com `pop()`, tamanho com `len()` e percursos com `for`.

### Análise de crédito

Simula uma decisão de crédito com base em renda, score, restrições e valor solicitado.

### Primeira API

Cria uma rota simples com FastAPI que retorna uma resposta em JSON.

## Como executar

### Requisitos

- Python 3 instalado
- FastAPI e Uvicorn apenas para executar o exercício de API

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/Matheus1807/Curso-dev.git
cd Curso-dev
```

Execute qualquer exercício informando seu caminho. Exemplos:

```bash
python condicionais/jogo.py
python loops/loja.py
python passaTempo/emprestimo.py
```

Para executar a API, instale as dependências necessárias:

```bash
python -m pip install fastapi uvicorn
python -m uvicorn passaTempo.api:app --reload
```

Depois, acesse `http://127.0.0.1:8000` no navegador.

## Objetivo

Meu objetivo com este repositório é praticar lógica de programação, consolidar os fundamentos de Python e acompanhar minha evolução por meio de exercícios progressivos e pequenos projetos.

## Próximos passos

- Criar funções para reutilizar trechos de código
- Melhorar o tratamento de entradas inválidas
- Estudar dicionários, tuplas e conjuntos
- Organizar dependências do projeto
- Criar novos endpoints na API
- Adicionar testes automatizados

## Tecnologia

- Python 3
- FastAPI

---

Desenvolvido para fins de estudo e prática de programação em Python.
