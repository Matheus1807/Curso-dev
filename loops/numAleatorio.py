# 3 rodadas contra a máquina para adivinhar 
#  um número secreto entre 1 e 50.
import random

print(
    "O jogo é o seguinte:\n"
    "3 rodadas contra a máquina para adivinhar o número\n"
    "que ela escolheu de 1 a 50."
)

jogador = int(input("Escolha numero: "))
computador = random.randint(1,50)
tentativas = 0   

if jogador == computador:

    print(
        "Você ganhou!\n"
        "Conseguiu 100 pontos!"
        )

while(tentativas < 5):
    tentativas+=1 

    print(f' Você está {tentativas} ')

    if  jogador == computador:

        print(
        "Você ganhou!\n"
        f"O número era {computador}\n"
        "Conseguiu 100 pontos!"
        )

        break

    elif jogador != computador:
        print("Você errou, jogue de novo!")
        jogador = int(input("Escolha numero:"))

computador = random.randint(1,50)
tentativas = 0  

print("A segunda - valendo 75 pnts ")

while(tentativas < 5):
    tentativas+=1 

    print(f' Você está {tentativas} ')

    if  jogador == computador:

        print(
        "Você ganhou!\n"
        f"O número era {computador}\n"
        "Conseguiu 100 pontos!"
        )

        break

    elif jogador != computador:
        print("Você errou, jogue de novo!")
        jogador = int(input("Escolha numero:"))



computador = random.randint(1,50)        
tentativas = 0  
print("A terceira rodada")
while(tentativas < 5):
    tentativas+=1 

    print(f' Você está {tentativas} ')

    if  jogador == computador:

        print(
        "Você ganhou!\n"
        f"O número era {computador}\n"
        "Conseguiu 100 pontos!"
        )

        break

    elif jogador != computador:
        print("Você errou, jogue de novo!")
        jogador = int(input("Escolha numero:"))


else:
    print("Suas tentativas acabaram.")