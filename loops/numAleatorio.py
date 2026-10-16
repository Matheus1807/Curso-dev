# 3 rodadas contra a máquina para adivinhar 
#  um número secreto entre 1 e 50.
import random

print(
    "O jogo é o seguinte:\n"
    "3 rodadas contra a máquina para adivinhar o número\n"
    "que ela escolheu de 1 a 50."
)
pontos = 0

for i in range(3):
    computador = random.randint(1,50)
    print(f'rodas é igual {i+1}')
    tentativas = 0  

    while(tentativas < 5):
        jogador = int(input("Escolha numero: "))   
        tentativas+=1 

        print(f' Você está {tentativas} ')

        if  jogador == computador:

            print(
            "Você ganhou!\n"
            f"O número era {computador}\n"
            "Conseguiu 100 pontos!"
            )
            break

        elif jogador > computador:
            print('número menor')

        elif jogador < computador:
            print('número maior')


    print("Suas tentativas acabaram.")
    computador = random.randint(1,50)