# Construa um programa que só aceite notas escolares entre zero e dez
nota = float(input(
    "Digite a primeira nota: "))

while (nota < 0 or nota > 10) :
    print("Digite uma nota valida")
    nota = float(input(
        "Digite a primeira nota: "))

# while not (nota >= 0 or nota <= 10) :

print("nota valida")