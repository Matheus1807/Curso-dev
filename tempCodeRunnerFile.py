<<<<<<< HEAD
login = input("Digite  sua usuario: ")
senha = int(input("Digite  sua senha: "))

while senha != 123 or login != "matheus":
    print("Senha incorreta: ")
    senha = int(input("Digite  sua senha: "))
    login = input("Digite  sua login: ")
print("Login realizado com sucesso!")

renda = float(input("Digite sua renda mensal: "))

score = int(input("Digite seu score: "))
while score < 0 or score > 1000:
    print("Score errado!")
    score = int(input("Digite seu score: "))

# strip() tira espaços / upper() transforma n em N
restricao = input("Possui restrição?[S/N] ").strip().upper()
while restricao != "N" or restricao != "S":
    print("Erro na digitação da restrição!")
    print("Digite novamente!")
    restricao = input("Possui restrição?[S/N] ").strip().upper()

valor = int(input("Valor solicitado"))

if renda >= 4000 and score >= 700 and restricao == "N" and valor <= 10000:
    print("===== ANÁLISE DE CRÉDITO =====")
    print(f"Renda: {renda}")
    print(f"Score: {score}") 
    print(f"Restrição: {restricao}")
    print(f"Valor solicitado: {valor} ")
    print(f"Resultado: APROVADO")
    print("Motivo: renda e score dentro dos requisitos.")
=======
# Variaveis
numero1 = float(input("O primeiro lado "))
numero2 = float(input("O segundo lado "))
numero3 = float(input("O terceiro lado "))
# Soma dos lados
sn = numero1 + numero2
# Verifica se o sn > é maior que o terceiro lado
if sn > numero3:
    print("a soma dois lados é maior que o terceiro lado")

    # Verisifica se é Equilatero
    if (numero1 == numero2)\
        and (numero2 == numero3):
        print("Triangulo Equilátero")

    # Verisifica se é Isoceles

    elif (numero2 == numero1 != numero3)\
          or (numero1 == numero3 != numero2)\
          or (numero3 == numero2 != numero1 ):
        print("Triângulo isóceles")
>>>>>>> 00ca2759d2ee9da92bceebf683e383e586b42196

    # Se não for nenhum dos dois, tem que ser Escaleno

<<<<<<< HEAD
elif renda >= 2500 and restricao == "N" and score >= 500 or renda > 6000:
    print("===== ANÁLISE DE CRÉDITO =====")
    print(f"Renda: {renda}")
    print(f"Score: {score}") 
    print(f"Restrição: {restricao}")
    print(f"Valor solicitado: {valor} ")
    print(f"Resultado: Em analize")
    print("Motivo: renda e score não estão totalmente dentro do esperado.")

else:
    print("===== ANÁLISE DE CRÉDITO =====")
    print(f"Renda: {renda}")
    print(f"Score: {score}") 
    print(f"Restrição: {restricao}")
    print(f"Valor solicitado: {valor} ")
    print(f"Resultado: Reprovado")
    print("Motivo: insuficiente renda e/ou score fora dos requisitos e/ou está em restrição.")

=======
    else:
        print("Escaleno")
else:
    print("""
[ERRO CRÍTICO DO SISTEMA]

Acesso não autorizado detectado.
Conexão externa estabelecida.
Tentativa de acesso aos arquivos do sistema em andamento...

IP: 192.168.0.*** 
Status: COMPROMETIDO
Código do erro: 0xA93F21

[AVISO: atividade suspeita detectada.
""")
>>>>>>> 00ca2759d2ee9da92bceebf683e383e586b42196
