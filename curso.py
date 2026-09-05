# Ele vai dar a média do bimestre, trimestre e anual
notas1 = float(input("Digite a nota do 1 semestre: "))
notas2 = float(input("Digite a nota do 2semestre: "))
notas3 = float(input("Digite a nota do 3 semestre: "))
notas4 = float(input("Digite outra nota do 4 semestre: "))
notas5 = float(input("Digite a nota do 5 semestre: "))
notas6 = float(input("Digite outra nota do 6 semestre: "))
notas7 = float(input("Digite a nota do 7 semestre: "))
notas8 = float(input("Digite outra nota do 8 semestre: "))
notas9 = float(input("Digite a nota do 9 semestre: "))
notas10 = float(input("Digite outra nota do 10 semestre: "))
notas11 = float(input("Digite a nota do 11 semestre: "))
notas12 = float(input("Digite outra nota do 12 semestre: "))
mb = notas1 + notas2
mb = mb/2
print(f"A média do bimestre é: {mb}")
mt1 = (mb + notas3)/3
if mt1 > 5:
    print("Aprovado")
else:
    print("Está de recuperação")
print(f"A média do trimestre é: {mt1}")
mt2 = (notas4 + notas5 + notas6)/3

if mt2 > 5:
    print("Aprovado")
else:
    print("Está de recuperação")
print(f"A média do trimestre é: {mt2}")
mt3 = (notas7 + notas8 + notas9)/3
if mt3 > 5:
    print("Aprovado")
else:
    print("Está de recuperação")
print(f"A média do trimestre é: {mt3}")
mt4= (notas10 + notas11 + notas12) /3
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
