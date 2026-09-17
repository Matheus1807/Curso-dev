# 3 rodadas contra a máquina para adivinhar 
#  um número secreto entre 1 e 50.
import random

jogador = int(input("Escolha numero: "))
computador = random.randint(0,50)
tentativas = 0
pontos = 0

if jogador == computador:
    print("Você ganhou")

while(tentativas < 4):
    tentativas+=1 
    print(f'Tentativa é: {tentativas}')
    if  jogador == computador:
        print(jogador)
        print(computador)
        print("Ganhou")
        pontos = 100
    elif jogador != computador:
        print(jogador)
        print(computador)
        jogador = int(input("Escolha numero:"))

tentativas = 0  
print("A segunda - valendo 75 pnts ")
while(tentativas < 5):
    rodadas+=1
    tentativas+=1 
    print(f'Tentativas é: {tentativas}')
    if  jogador == computador:
        print(jogador)
        print(computador)
        print("Ganhou")
    elif jogador != computador:
        print(jogador)
        print(computador)
        jogador = int(input("Escolha numero:"))
        
tentativas = 0  
print("A terceira rodada")
while(tentativas < 5):
    rodadas+=1
    tentativas+=1 
    print(f'Tentativas é: {tentativas}')
    if  jogador == computador:
        print(jogador)
        print(computador)
        print("Ganhou")
    elif jogador != computador:
        print(jogador)
        print(computador)
        jogador = int(input("Escolha numero:"))
    