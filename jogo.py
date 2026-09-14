import random
opção = ["pedra", 'papel', 'tesoura']
computador = random.choice(opção)
jogador = input("Escolha um: ")
print(f"Computador escolheu: {computador}")
if jogador == computador:
    print("Empate")
elif (
    (jogador == "pedra" and computador == "tesoura")
    or (jogador == "papel" and computador == "pedra")
    or (jogador == "tesoura" and computador == "papel")
):
    print("Você ganhou")
elif jogador in opção:
    print("Computador ganhou")
else:
    print("Opção invalida")
