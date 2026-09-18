# Ele vai dar a média do bimestre, trimestre e anual com base nas notas dadas
notas = []

for i in range(1, 14):
    nota = float(input(f"Digite a {i}ª nota: "))

    while nota < 0 or nota > 10:
        print("Nota inválida")
        nota = float(input("Digite novamente: "))
    notas.append(nota)


mb = notas[0] + notas[1]
mb = mb/2
print(f"A média do bimestre é: {mb}")
mt1 = (mb + notas[3])/3
if mt1 > 5:
    print("Aprovado")
else:
    print("Está de recuperação")
print(f"A média do trimestre é: {mt1}")
mt2 = (notas[4] + notas[5] + notas[6])/3

if mt2 > 5:
    print("Aprovado")
else:
    print("Está de recuperação")
print(f"A média do trimestre é: {mt2}")
mt3 = (notas[7] + notas[8] + notas[9])/3
if mt3 > 5:
    print("Aprovado")
else:
    print("Está de recuperação")
print(f"A média do trimestre é: {mt3}")
mt4= (notas[10] + notas[11] + notas[12]) /3
if mt4 > 5:
    print("Aprovado")
else:
    print("Está de recuperação")
print(f"A média do trimestre é: {mt4}")
mAnual = (mt1 + mt2 + mt3 + mt4)/4
print(f"A média anual é: {mAnual}")
if mAnual > 5:
    print("Aprovado")
else:
    print("Reprovado")
