# 📊 Calculadora de Médias Escolares

Projeto simples desenvolvido em **Python** para calcular médias escolares a partir das notas informadas pelo usuário.

O programa solicita as notas, verifica se elas estão entre **0 e 10** e calcula as médias do bimestre, dos trimestres e a média anual.

## 🚀 Funcionalidades

- Recebe as notas pelo terminal
- Armazena as notas em uma lista
- Valida notas entre `0` e `10`
- Não permite continuar enquanto uma nota inválida for informada
- Calcula a média bimestral
- Calcula as médias trimestrais
- Calcula a média anual
- Informa se o aluno está:
  - Aprovado
  - Em recuperação
  - Reprovado ao final do ano

## 🧠 Conceitos utilizados

Durante o desenvolvimento foram utilizados conceitos básicos de Python, como:

- Variáveis
- `input()`
- `float()`
- Listas
- `for`
- `range()`
- `while`
- `append()`
- Condições com `if` e `else`
- Operadores matemáticos
- Operadores lógicos `or`
- F-strings

## 💻 Código

```python
# Ele vai dar a média do bimestre, trimestre e anual com base nas notas dadas

notas = []

for i in range(1, 14):
    nota = float(input(f"Digite a {i}ª nota: "))

    while nota < 0 or nota > 10:
        print("Nota inválida")
        nota = float(input("Digite novamente: "))

    notas.append(nota)


mb = notas[0] + notas[1]
mb = mb / 2

print(f"A média do bimestre é: {mb}")


mt1 = (mb + notas[3]) / 3

if mt1 > 5:
    print("Aprovado")
else:
    print("Está de recuperação")

print(f"A média do trimestre é: {mt1}")


mt2 = (notas[4] + notas[5] + notas[6]) / 3

if mt2 > 5:
    print("Aprovado")
else:
    print("Está de recuperação")

print(f"A média do trimestre é: {mt2}")


mt3 = (notas[7] + notas[8] + notas[9]) / 3

if mt3 > 5:
    print("Aprovado")
else:
    print("Está de recuperação")

print(f"A média do trimestre é: {mt3}")


mt4 = (notas[10] + notas[11] + notas[12]) / 3

if mt4 > 5:
    print("Aprovado")
else:
    print("Está de recuperação")

print(f"A média do trimestre é: {mt4}")


mAnual = (mt1 + mt2 + mt3 + mt4) / 4

print(f"A média anual é: {mAnual}")

if mAnual > 5:
    print("Aprovado")
else:
    print("Reprovado")
```

## ▶️ Como executar

Tenha o Python instalado no computador.

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd Curso-dev
```

Execute o arquivo:

```bash
python curso.py
```

## 📝 Exemplo

```text
Digite a 1ª nota: 8
Digite a 2ª nota: 7
Digite a 3ª nota: 9
...
```

Caso seja digitada uma nota inválida:

```text
Digite a 1ª nota: 15
Nota inválida
Digite novamente: 8
```

O programa somente aceita notas entre `0` e `10`.

## 🎯 Objetivo do projeto

Este projeto foi criado com o objetivo de praticar os fundamentos de Python, principalmente estruturas de repetição, listas, condições e validação de dados.

## 🛠️ Tecnologia

- Python 3

## 📚 Aprendizados

Com este projeto foi possível praticar como armazenar vários valores dentro de uma lista e utilizar estruturas como `for` e `while` para evitar repetição desnecessária de código.

---

Projeto desenvolvido para fins de estudo e prática de **Python**.
