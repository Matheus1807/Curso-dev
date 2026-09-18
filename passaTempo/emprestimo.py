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
while restricao != "N" and restricao != "S":
    print("Erro na digitação da restrição!")
    print("Digite novamente!")
    restricao = input("Possui restrição?[S/N] ").strip().upper()

valor = int(input("Valor solicitado"))

if renda >= 4000 and score >= 700 and \
    restricao == "N" and valor <= 10000:
    print("===== ANÁLISE DE CRÉDITO =====")
    print(f"Renda: {renda}")
    print(f"Score: {score}") 
    print(f"Restrição: {restricao}")
    print(f"Valor solicitado: {valor} ")
    print(f"Resultado: APROVADO")
    print("Motivo: renda e score dentro dos requisitos.")


elif restricao == "N" and (
    renda >= 2500 and score >= 500
    or renda > 6000
):
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

