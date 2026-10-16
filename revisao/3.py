# Exercício 3: Análise Térmica Semanal e Filtro de Desvio
# Implemente um programa que receba as temperaturas médias registradas durante
# os 7 dias da semana (armazenadas em um vetor de números reais). O programa
# deve calcular a média aritmética semanal e, em seguida, exibir quais temperaturas
# registradas ficaram estritamente abaixo dessa média.
lista = []
dia = 0
while not (dia == 7):
    nota = int(input(f"Digite a temperatura em graus:  "))
    lista.append(nota)
    dia += 1
media = max(lista)/2
menores = []
for numero in lista:
    if numero < media:
        menores.append(numero)
print(f'A media foi: {media}, e as temperaturas que ficou estritamente abaixo dessa média fora: {menores} ')